from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from twisted.internet import reactor
from twisted.web import server, resource

import json

engine = create_engine('sqlite:///test.db')

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('notes.id'), nullable=True)
    
    url = Column(Text, nullable=True)
    note = Column(Text)
    position = Column(String(255))
    
    created = Column(DateTime, default=datetime.now)
    
    replies = relationship("Note")
    
    def __init__(self, url, note, position=''):
        self.url, self.note, self.position = url, note, position
    
    def __repr__(self):
        return '[note]'

Base.metadata.create_all(engine) 

Session = sessionmaker()
Session.configure(bind=engine)

class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime): return str(obj)
        o = {'id':obj.id, 'note':obj.note, 'created':obj.created} #,'parent_id':obj.parent_id}
        
        if obj.position: o['position'] = obj.position
        if obj.parent_id: o['parent_id'] = obj.parent_id
        
        if obj.replies: o['replies'] = [self.default(m) for m in obj.replies]
        
        return o
        
class NoteResource(resource.Resource):
    isLeaf = True
    
    def render_GET(self, request):
        request.setHeader("content-type", "application/json")
        self.setHeaders(request)
        
        if not request.args.has_key('url'):
            return ''
            
        parent_id = request.args['child_of'][0] if request.args.has_key('child_of') else None
        
        posts = Session().query(Note).filter(Note.url == request.args['url'][0]).filter(Note.parent_id == parent_id).all()
        
        return json.dumps(posts, cls=NoteEncoder)
    
    def setHeaders(self, request):
	    request.setHeader('Access-Control-Allow-Origin','*')
	    request.setHeader('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
	    request.setHeader('Access-Control-Max-Age', 1000)
	    request.setHeader('Access-Control-Allow-Headers', '*')
    
    def render_POST(self, request):
        session = Session()
        self.setHeaders(request)
        
        url = request.args['url'][0]
        note = request.args['note'][0]
        
        n = Note(url, note)
        
        if request.args.has_key('position'): n.position = request.args['position'][0]
        if request.args.has_key('reply_to'): n.parent_id = request.args['reply_to'][0]
        
        session.add(n)
        session.commit()
        
        request.setHeader("content-type", "application/json")
        return json.dumps(n, cls=NoteEncoder)

reactor.listenTCP(8080, server.Site(NoteResource()))
reactor.run()
