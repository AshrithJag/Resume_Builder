# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    #data1=db(db.auth_user.id==auth.user.id).select(db.auth_user.choose)
    #if data1[0].choose!='company':
  
    if auth.user:
        redirect(URL(r=request , f='checkingcompany' ))    
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def index_new():
    return dict()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_login()
def companycheck():
	data1=db(db.auth_user.id==auth.user.id).select(db.auth_user.choose)
	if data1[0].choose!='company' :
		data4=db(db.profile1.stid==auth.user.id).select(db.profile1.stid)
		data5=db(db.profile2.stid==auth.user.id).select(db.profile1.stid)
		data6=db(db.profile4.stid==auth.user.id).select(db.profile1.stid)
		if len(data4) > 0 :
			if len(data5) > 0 :
				if len(data6) > 0:
					redirect(URL(r=request , f='seeingstudentprofile',args=auth.user.id ))
				else:
					redirect(URL(r=request , f='buildingstudentprofile2' ))
			else :
				redirect(URL(r=request , f='buildingstudentprofile1' ))
		else:
			redirect(URL(r=request , f='buildingstudentprofile' ))
	else :
		data=db(db.companyprofile.stid==auth.user.id).select(db.companyprofile.stid)
		if len(data) > 0 :
			redirect(URL(r=request , f='seeingcompanyprofile' ))
		else:
			redirect(URL(r=request , f='buildingcompanyprofile' ))
	return dict()
	
import cStringIO
 
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate():
    """
    To display the generated PDF in your browser go to:
     http://.../<app>/<controller>/generate
     
    To download it as hello.pdf, for example, instead, use:
     http://.../<app>/<controller>/generate/hello.pdf
    """
    text=db(auth.user.id==db.profile1.stid).select(db.profile1.first_name)
    tad=db(auth.user.id==db.profile1.stid).select(db.profile1.chirunama)
    tph=db(auth.user.id==db.profile1.stid).select(db.profile1.phoneno)
    tpp=db(auth.user.id==db.profile1.stid).select(db.profile1.profilepic)
    tcour=db(auth.user.id==db.profile3.stid).select(db.profile3.course)
    tcol=db(auth.user.id==db.profile3.stid).select(db.profile3.collegename)
    tcg=db(auth.user.id==db.profile3.stid).select(db.profile3.cgpa)
    tsc=db(auth.user.id==db.profile2.stid).select(db.profile2.schoolname)
    tper=db(auth.user.id==db.profile2.stid).select(db.profile2.percentage)
    tis=db(auth.user.id==db.profile4.stid).select(db.profile4.istam)
    tpr=db(auth.user.id==db.profile4.stid).select(db.profile4.projects)
    tcom=db(auth.user.id==db.profile5.stid).select(db.profile5.workedin)
    twrk=db(auth.user.id==db.profile5.stid).select(db.profile5.post)
    tex=db(auth.user.id==db.profile5.stid).select(db.profile5.pani)
    styles = getSampleStyleSheet()
    story = [
    Paragraph("RESUME",styles['Title']),
    Spacer(1,0.25*inch),
    Paragraph("General Info",styles['Title']),
    Paragraph("-"*70,styles['Title']),
    Paragraph("Name:"+text[0].first_name, styles['Heading4']),
    Paragraph("Address:"+tad[0].chirunama, styles['Heading4']),
    Paragraph("Email id:"+auth.user.email, styles['Heading4']),
    Paragraph("Contact no:"+tph[0].phoneno, styles['Heading4']),
    Paragraph('-'*70,styles['Title']),
    Paragraph('Other Info.',styles['Title']),
    Paragraph("School:"+tsc[0].schoolname, styles['Heading4']),
   # Paragraph(tsc[0].schoolname,styles['Normal']),
    Paragraph("Percentage(10th Finals):"+str(tper[0].percentage), styles['Heading4']),
    #Paragraph(str(tper[0].percentage),styles['Normal']),
    Paragraph("Hobbies:"+tis[0].istam, styles['Heading4']),
   # Paragraph(tis[0].istam,styles['Normal']),
    Paragraph("Projects/Works:"+tpr[0].projects, styles['Heading4']),
    #Paragraph(tpr[0].projects,styles['Normal']),
    Paragraph('-'*70,styles['Title']),
    Paragraph("Work Experience", styles['Title']),
    ]
    for i in range(len(tcom)):
        story.append(
        Paragraph("Company"+'\t\t : \t\t'+tcom[i].workedin,styles['Heading4']))
        
        story.append(
    Paragraph("Worked as"+'\t\t : \t\t'+twrk[i].post, styles['Heading4']))
        
        
        story.append(
    Paragraph("Worked for(years)"+'\t\t : \t\t'+str(tex[i].pani), styles['Heading4']))
       
        story.append(
    Paragraph("-"*30,styles['Heading4'])
    )
    story.append(Paragraph("College(s)",styles['Title']))
    story.append(
    Paragraph("-"*70,styles['Title']))
    for i in range(len(tcour)):
        story.append(
    Paragraph("Branch:"+tcour[i].course, styles['Heading4']))
       
        story.append(
    Paragraph("University/College:"+tcol[i].collegename, styles['Heading4']))
        
        story.append(
    Paragraph("CGPA:"+str(tcg[i].cgpa), styles['Heading4']))
        story.append(
    Paragraph("-"*30,styles['Heading4']))
    story.append(
    Paragraph("-"*70,styles['Title']))
    buffer = cStringIO.StringIO()   
    doc = SimpleDocTemplate(buffer)
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
      
    filename = request.args(0)
    if filename:
        header = {'Content-Disposition': 'attachment; filename=' + filename}
    else:
        header = {'Content-Type': 'application/pdf'}
    response.headers.update(header)
    return pdf
def trya():
    return dict()
def listing():
    text=db(auth.user.id==db.profile1.stid).select(db.profile1.first_name)
    tad=db(auth.user.id==db.profile1.stid).select(db.profile1.chirunama)
    tph=db(auth.user.id==db.profile1.stid).select(db.profile1.phoneno)
    tpp=db(auth.user.id==db.profile1.stid).select(db.profile1.profilepic)
    tcour=db(auth.user.id==db.profile3.stid).select(db.profile3.course)
    tcol=db(auth.user.id==db.profile3.stid).select(db.profile3.collegename)
    tcg=db(auth.user.id==db.profile3.stid).select(db.profile3.cgpa)
    tsc=db(auth.user.id==db.profile2.stid).select(db.profile2.schoolname)
    tper=db(auth.user.id==db.profile2.stid).select(db.profile2.percentage)
    tis=db(auth.user.id==db.profile4.stid).select(db.profile4.istam)
    tpr=db(auth.user.id==db.profile4.stid).select(db.profile4.projects)
    tcom=db(auth.user.id==db.profile5.stid).select(db.profile5.workedin)
    twrk=db(auth.user.id==db.profile5.stid).select(db.profile5.post)
    tex=db(auth.user.id==db.profile5.stid).select(db.profile5.pani)
    tpy=db(auth.user.id==db.profile3.stid).select(db.profile3.passoutyear)
    response.title = "web2py sample listing"
    
    # define header and footers:
    head = THEAD(TR(TH("Header 1",_width="30%"), 
                    TH("Header 2",_width="30%"),              
                    _bgcolor="#A0A0A0"))
    foot = TFOOT(TR(TH("Footer 1",_width="30%"), 
                    TH("Footer 2",_width="30%"),
                    _bgcolor="#E0E0E0"))
    
    # create several rows:
    rows = []
    col = 1 and "#F0F0F0" or "#FFFFFF"
    rows.append(TR(TD("First Name", _align="center"),
                       TD(text[0].first_name,_align="left"),
                       _bgcolor=col)) 
    rows.append(TR(TD("Address", _align="center"),
                       TD(tad[0].chirunama,_align="left"),
                       _bgcolor=col)) 
    rows.append(TR(TD("First Name", _align="center"),
                       TD(text[0].first_name,_align="center"),
                       _bgcolor=col)) 
    # make the table object
    body = TBODY(*rows)
    table = TABLE(*[head,foot, body], 
                  _border="2", _width="100%")

    if request.extension=="pdf":
        from gluon.contrib.pyfpdf import FPDF, HTMLMixin

        # define our FPDF class (move to modules if it is reused  frequently)
        class MyFPDF(FPDF, HTMLMixin):
            def header(self):
                self.set_font('Arial','B',25)
                self.cell(0,10,'Resume',1,0,'C')
                self.ln(30)
            def head(self,txt):
                self.set_font('Times','B',20)
                self.cell(0,10, txt ,0,0,'C')
                self.ln(20)
            def head1(self,txt):
                self.set_font('Helvetica','B',17)
                self.cell(0,10, txt ,0,0,'C')
                self.ln(20)
            def bodybig(self,txt1,txt2):
                self.set_font('Helvetica','B',15)
                self.cell(0,10, txt1 ,0,0,'L')
                #self.cell(0,-300, ':', 0 ,0, 'R')
                self.set_font('Helvetica','',10)
                self.cell(-150,10, txt2 ,0,0,'C')
                self.ln(12)
            def body(self,txt1,txt2):
                self.set_font('Helvetica','B',15)
                self.cell(0,10, txt1 ,0,0,'L')
                #self.cell(0,-300, ':', 0 ,0, 'R')
                self.set_font('Helvetica','',10)
                self.cell(-250,10, txt2 ,0,0,'C')
                self.ln(12)
            def body1(self,txt1,txt2):
                self.set_font('Helvetica','B',20)
                self.cell(0,10, txt1 ,0,0,'L')
                #self.cell(0,-300, ':', 0 ,0, 'R')
                self.set_font('Helvetica','I',10)
                self.cell(-150,10, txt2 ,0,0,'C')
                self.ln(12)
            def bodynew(self,txt1,txt2):
                self.set_font('Helvetica','B',15)
                self.cell(0,10, txt1 ,0,0,'L')
                #self.cell(0,-300, ':', 0 ,0, 'R')
                self.set_font('Helvetica','',10)
                for i in range(len(txt2)):
                    self.cell(-250,10, txt2[i] ,0,0,'C')
                self.ln(12)
            def img(self,img):
                self.image(img,10,8,33);
                self.ln(15)
            def add(self,txt1,temp):
                self.set_font('Helvetica','B',15)
                self.cell(0,10, txt1 ,0,0,'L')
                #self.cell(0,-300, ':', 0 ,0, 'R')
                self.set_font('Helvetica','',10)
                for i in temp:
                    self.cell(-150,10, str(i) ,0,0,'C')
                    self.ln(12)
            def footer(self):
                self.set_y(-15)
                self.set_font('Times','I',12)
                txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
                self.cell(0,10,txt,0,0,'C')
                    
        pdf=MyFPDF()
        # first page:
        pdf.add_page()
        #pdf.write_html(str(XML(table, sanitize=False)))
        #pdf.header()
        #pdf.img(tpp[0].profilepic)
        tem=[]
        tem=(tad[0].chirunama).split(',')
        
        pdf.head('General Info.')
        pdf.body('First name',text[0].first_name)
        pdf.bodybig('Address',tad[0].chirunama)
        pdf.body('Email id',auth.user.email)
        pdf.body('Phone no.', tph[0].phoneno)
        pdf.bodybig('Description', tis[0].istam)
        #pdf.bodynew('Description', tis[0].istam)
        pdf.head('Other Info.')
        pdf.body('School',tsc[0].schoolname)
        pdf.body('10th Final Grade',str(tper[0].percentage))
        pdf.ln(15)
        pdf.head('Work Experience')
        for i in range(len(tcom)):
             pdf.head1('#'+str(i+1)+' '+tcom[i].workedin)
             pdf.body('Post',twrk[i].post)
             pdf.body('Worked for',str(tex[i].pani)+' '+'Years')
             pdf.ln(15)
        pdf.ln(15)
        for i in range(len(tcour)):
             pdf.head1('#'+str(i+1)+' '+tcol[i].collegename)
             pdf.body('Branch',tcour[i].course)
             pdf.body('CGPA',str(tcg[i].cgpa))
             pdf.body('Passoutyear',str(tpy[0].passoutyear))
             pdf.ln(15)
        pdf.body1('Projects',tpr[0].projects)
        #pdf.footer()
        #
        response.headers['Content-Type']='application/pdf'
        #filename = request.args(0)
        #if filename:
         #   header = {'Content-Disposition': 'attachment; filename=' + filename}
       # else:
        #    header = {'Content-Type': 'application/pdf'}
        #response.headers.update(header)
        return pdf.output(dest='S')
       # return pdf.output(dest='S')
        #else:
        # normal html view:
        #return dict(table=table)
            
def seeingcompanyprofile():
	data=db(db.companyprofile.stid==auth.user.id).select()
	return dict(data=data)



def seeingstudentprofile():
	r=request.args(0)
	data1=db(db.profile1.stid==r).select()
	data2=db(db.profile2.stid==r).select()
	data3=db(db.profile4.stid==r).select()
	data5=db(db.profile5.stid==r).select()
	data4=db(db.profile3.stid==r).select()
	return dict(data1=data1,data2=data2,data3=data3,data4=data4,data5=data5)


@auth.requires_login()
def buildingstudentprofile():
	form=SQLFORM(db.profile1, deletable=True, fields=['first_name','last_name','father_name','chirunama','phoneno','profilepic'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='buildingstudentprofile1' ))
	return dict(form=form)

def buildingstudentprofile1():
	form=SQLFORM(db.profile2,deletable=True,fields=['schoolname','passoutyear','percentage'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='buildingstudentprofilemain' ))
	return dict(form=form)
def buildingstudentprofile2():
	form=SQLFORM(db.profile4,deletable=True,fields=['istam','projects'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='checkingcompany' ))
	return dict(form=form)

def buildingstudentprofile5():
	form=SQLFORM(db.profile5,deletable=True,fields=['workedin','post','pani'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='index' ))
	return dict(form=form)

def buildingstudentprofilemain():
	form=SQLFORM(db.profile3,deletable=True,fields=['collegename','course','passoutyear','cgpa'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='testingpage' ))
	return dict(form=form)
def buildingstudentprofile555():
	form=SQLFORM(db.profile5,deletable=True,fields=['workedin','post','pani'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='testingpage555' ))
	return dict(form=form)
def testingpage():
	return dict()
def testingpage555():
	return dict()
def buildingcompanyprofile():
	form=SQLFORM(db.companyprofile,deletable=True,fields=['name','country','workers','states','chairperson'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='index' ))
	return dict(form=form)

def updatingcompanyprofile():
	data=db(db.companyprofile.stid==auth.user.id).select(db.companyprofile.id)
	record=data[0].id
	form = crud.update(db.companyprofile, record,fields=['name','country','workers','states','chairperson'],deletable=False,next = URL(r=request, f='index'))
	return dict(form=form)
def updatingstudentprofile1():
	data=db(db.profile1.stid==auth.user.id).select(db.profile1.id)
	if len(data):
		record=data[0].id

		form = crud.update(db.profile1, record,fields=['first_name','last_name','father_name','chirunama','phoneno','profilepic'],deletable=False,next = URL(r=request, f='updatingstudentprofile2'), _class="btn btn-primary")
	else :
		redirect(URL(r=request , f='buildingstudentprofile' ))
	return dict(form=form)
def updatingstudentprofile2():
	data=db(db.profile2.stid==auth.user.id).select(db.profile2.id)
	if len(data):
		record=data[0].id
		form = crud.update(db.profile2, record,fields=['schoolname','passoutyear','percentage'],deletable=False,next = URL(r=request, f='checkpage'), _class="btn btn-primary")
	else :
		redirect(URL(r=request , f='buildingstudentprofile1' ))
	return dict(form=form)
def updatingstudentprofile3():
	data=db(db.profile4.stid==auth.user.id).select(db.profile4.id)
	if len(data):
		record=data[0].id
		form = crud.update(db.profile4, record,fields=['istam','projects'],deletable=False,next = URL(r=request, f='checkingcompany') ,_class="btn btn-primary")
	else :
		redirect(URL(r=request , f='buildingstudentprofile2' ))
	return dict(form=form)

def checkpage():
	data=db(db.profile3.stid==auth.user.id).select(db.profile3.id)
	datae1=db(db.profile3.stid==auth.user.id).select()
	print len(data)
	if len(data)==0:
		redirect(URL(r=request , f='buildingstudentprofilemaincopy' ))
	return dict(datae1=datae1)

def checkpage555():
	data=db(db.profile5.stid==auth.user.id).select(db.profile5.id)
	datae1=db(db.profile5.stid==auth.user.id).select()
	print len(data)
	if len(data)==0:
		redirect(URL(r=request , f='buildingstudentprofile555copy' ))
	return dict(datae1=datae1)

def buildingstudentprofilemaincopy():
	form=SQLFORM(db.profile3,deletable=True,fields=['collegename','course','passoutyear','cgpa'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='checkpage' ))
	return dict(form=form)
def buildingstudentprofilemaincopyforinsert():
	form=SQLFORM(db.profile3,deletable=True,fields=['collegename','course','passoutyear','cgpa'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='checkingcompany' ))
	return dict(form=form)

@auth.requires_login()
def checkingcompany():
	data=db(db.auth_user.id==auth.user.id).select(db.auth_user.choose)
	if data[0].choose=='jobfinders':
		redirect(URL(r=request , f='studentsmainpage' ))
	else:
		redirect(URL(r=request , f='companymainpage' ))
	return dict(data=data)

def studentsmainpage():
    #data=db(db.notifye.id>0).select()
    return dict()#data=data)

def companymainpage():
	return dict()
	
def buildingstudentprofile555copy():
	form=SQLFORM(db.profile5,deletable=True,fields=['workedin','post','pani'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='checkpage555' ))
	return dict(form=form)

def buildingstudentprofile555copyforinsert():
	form=SQLFORM(db.profile5,deletable=True,fields=['workedin','post','pani'])
	form.vars.stid=auth.user.id			
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='checkingcompany' ))
	return dict(form=form)

def updatingstudentprofilemain():
	record=request.args[0]
	form = crud.update(db.profile3, record,fields=['collegename','course','passoutyear','cgpa'],deletable=False,next = URL(r=request, f='checkpage'),_class="btn btn-primary")
	return dict(form=form)

def updatingstudentprofile555():
	record=request.args[0]
	form = crud.update(db.profile5, record,fields=['workedin','post','pani'],deletable=False,next = URL(r=request, f='checkpage555') ,_class="btn btn-primary")
	return dict(form=form)

def mainpage():
	return dict()


def searching():
	form=SQLFORM.factory(
			db.Field('wordto',requires=IS_IN_SET(['Name','College','Work','CGPA','Company','highschool%','projects']),label='Keyword')
			)
	if form.accepts(request.vars,session):
		if form.vars.wordto=='Name' :
			redirect(URL(r=request , f='profile1checkname' ))
		if form.vars.wordto=='College' :
			redirect(URL(r=request , f='profile3college' ))			
		if form.vars.wordto=='Work' :
			redirect(URL(r=request , f='profile5pani' ))			
		if form.vars.wordto=='CGPA' :
			redirect(URL(r=request , f='profile3cgpa' ))			
		if form.vars.wordto=='Company' :
			redirect(URL(r=request , f='companyworkedin' ))			
		if form.vars.wordto=='highschool%' :
			redirect(URL(r=request , f='highschool' ))			
		if form.vars.wordto=='projects' :
			redirect(URL(r=request , f='project' ))			
	return dict(form=form)



import re
def profile1checkname():
	form=SQLFORM.factory(db.Field('wording'))
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='profile1checkname1', args=form.vars.wording ))
	return dict(form=form)

def profile1checkname1():
	data1=db(db.profile1.id>0).select()	
	data2=db(db.profile1.id>0).select()
	d4=[]
	d1=[]
	d2=[]
	d3={}
	d3['main']=request.args[0]
	for i in data1:
		if(re.search(request.args(0),i.first_name)):
			if d4.count(i.stid)==0:
				d1.append(i)
				d4.append(i.stid)
	for j in data2:
		if(re.search(request.args(0),j.last_name)):
			d2.append(j)
	return dict(d1=d1,d2=d2,d3=d3)


def profile3college():
	form=SQLFORM.factory(db.Field('wording'))
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='profile3college1', args=form.vars.wording ))
	return dict(form=form)


def profile3college1():
	data1=db(db.profile3.id>0).select()	
	d1=[]
	d2=[]
	d5=[]
	d3={}
	d3['main']=request.args[0]
	for i in data1:
		if(re.search(request.args(0),i.collegename)):
			if d5.count(i.stid)==0:
				d1.append(i)
				d5.append(i.stid)
	for j in d1:
		data2=db(db.profile1.stid==j.stid).select()
		d2.append(data2)
	return dict(d1=d1,d2=d2,d3=d3)




def profile5pani():
	form=SQLFORM.factory(db.Field('wording','double'))
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='profile5pani1', args=form.vars.wording ))
	return dict(form=form)




def profile5pani1():
	data1=db(db.profile5.id>0).select(orderby=db.profile5.stid)	
	data2=db(db.profile5.id>0).select(db.profile5.id ,orderby=db.profile5.id)
	d1=[]
	d1=[]
	d2={}
	d3=[]
	d4=[]
	d5={}
	d6=[]
	d5['main']=request.args[0]
	for m in data1:
		if d1.count(m.stid)==0:
			d1.append(m.stid)
			d4.append(m)
	for i in d4:
		data3=db(db.profile5.stid==i.stid).select()
		count=0
		d2={}
		for k in data3:
			if k.pani:
				count=count+k.pani
		print count
		print request.args[0]
		if count > float(request.args[0] ):
			d3.append(i)
			print 'yes'
	return dict(d3=d3,d5=d5)



def profile3cgpa():
	form=SQLFORM.factory(db.Field('wording','double'),
			)
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='profile3cgpa1', args=(form.vars.wording) ))
	return dict(form=form)


def profile3cgpa1():
	d3={}
	d3['main']=request.args[0]
	d5=[]
	data1=[]
	data2=db((db.profile3.cgpa > request.args(0) )).select(  orderby=db.profile3.stid )
	for i in data2:
		if d5.count(i.stid)==0:
			data1.append(i)
			d5.append(i.stid)
	return dict(data1=data1,d3=d3)


def companyworkedin():
	form=SQLFORM.factory(db.Field('wording'))
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='companyworkedin1', args=form.vars.wording ))
	return dict(form=form)

def companyworkedin1():
	data1=db(db.profile5.id>0).select()	
	d1=[]
	d2=[]
	d3={}
	d5=[]
	d3['main']=request.args[0]
	for i in data1:
		if(re.search(request.args(0),i.workedin)):
			if d5.count(i.stid):
				d1.append(i)
				d5.append(i.stid)
	for j in d1:
		data2=db(db.profile1.stid==j.stid).select()
		d2.append(data2)
	return dict(d1=d1,d2=d2,d3=d3)

def highschool():
	form=SQLFORM.factory(db.Field('wording','double'),
			)
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='highschool2', args=(form.vars.wording)))
	return dict(form=form)

def highschool2():

	d3={}
	d3['main']=request.args[0]
	data=db((db.profile2.percentage > request.args(0))).select()
	return dict(data=data,d3=d3)

def project():
	form=SQLFORM.factory(db.Field('wording'))
	if form.accepts(request.vars,session):
		redirect(URL(r=request , f='project1', args=form.vars.wording ))
	return dict(form=form)

def project1():
	data1=db(db.profile4.id>0).select()	
	d1=[]
	d2=[]
	d3={}
	d3['main']=request.args[0]
	a=request.args(0)
	b=a.replace('_',' ') 
	print b
	for i in data1:

		if(re.search(b,i.projects)):
			if d2.count(i.stid)==0 :
				d1.append(i)
	return dict(d1=d1,d3=d3)

def companyprofileview():
	a=request.args[0]
	dq={}
	data=db(db.profile1.stid==a).select()
	dq['return']=request.args[1]
	dq['main']=request.args[2]
	return dict(data=data,dq=dq)

def messaging():
	data=db(db.auth_user.id==auth.user.id).select(db.auth_user.username)
	form=SQLFORM(db.messaging,fields=['toe','subject','matter','filematter'], _class="btn btn-success")
	form.vars.frome=auth.user.username
	data1=db(db.auth_user.id > 0).select(db.auth_user.username)
	k=0
	if form.accepts(request.vars,session):
		value=form.vars.id
		count=0
		for i in data1:
			if i.username==form.vars.toe:
				count=1
				break
		if count==1:
		          redirect(URL(r=request , f='checkingcompany'))
		          
		else:
			response.flash=T('Invalid Username')
			db(db.messaging.id==value).delete()
    #LI(A("go back", _href=URL(r=request, f="companymainpage")))    
	return dict(form=form)
	
def showmessage():
	show=db(db.messaging.toe==auth.user.username).select()
	return dict(show=show)
def messagedetail():
	value=request.args[0]
	data=db(db.messaging.id==value).select()
	return dict(data=data)
def reply():

	data=db(db.auth_user.id==auth.user.id).select(db.auth_user.username)
	form=SQLFORM(db.messaging,fields=['subject','matter','filematter'],_class="btn btn-success")
	form.vars.frome=auth.user.username
	form.vars.toe=request.args(0)
	data1=db(db.auth_user.id > 0).select(db.auth_user.username)
	if form.accepts(request.vars,session):
		value=form.vars.id
		count=0
		for i in data1:
			if i.username==form.vars.toe:
				count=1
				break
		if count==1:
		          redirect(URL(r=request , f='showmessage'))
		else:
			db(db.messaging.id==value).delete()

	return dict(form=form)
	
def notice():
	data=db(db.auth_user.id==auth.user.id).select(db.auth_user.choose)
	form=SQLFORM.factory(db.Field('title'),
			db.Field('matter','text'),_class='btn btn-primary')
	if form.accepts(request.vars,session):
		db.notifye.insert(
				bye=auth.user.username,
				title=form.vars.title,
				matter=form.vars.matter
				)
		redirect(URL(r=request , f='checkingcompany'))
	return dict(form=form)
def seenotice():
	data=db(db.notifye.id>0).select()
	return dict(data=data)
def notc():
    return dict()
def seeingnicenotice():
	value=request.args[0]
	vc=db(db.notifye.id==value).select()
	return dict(vc=vc)
def delnotice():
    val=request.args[0]
    db(db.notifye.id==val).delete()
    redirect(URL(r=request , f='companymainpage'))
def dnotice():
    val=auth.user.username
    v1=db((db.notifye.bye==val) & (db.notifye.id>0)).select(db.notifye.id)
    v2=db((db.notifye.bye==val) & (db.notifye.id>0)).select(db.notifye.title)
    v3=db((db.notifye.bye==val) & (db.notifye.id>0)).select(db.notifye.matter)
    return dict(v1=v1,v2=v2,v3=v3)
def ntc():
    val=auth.user.username
    v1=db((db.notifye.bye==val) & (db.notifye.id>0)).select(db.notifye.id,db.notifye.title,db.notifye.matter)
    v2=db((db.notifye.bye==val) & (db.notifye.id>0)).select(db.notifye.title)
    v3=db((db.notifye.bye==val) & (db.notifye.id>0)).select(db.notifye.matter)
    return dict(v1=v1,v2=v2,v3=v3)
@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())



def seeingstudentprofile111():
	r=request.args(0)
	data1=db(db.profile1.stid==r).select()
	data2=db(db.profile2.stid==r).select()
	data3=db(db.profile4.stid==r).select()
	return dict(data1=data1,data2=data2,data3=data3)

def reply1():
    data=db(db.auth_user.id==auth.user.id).select(db.auth_user.username)
    form=SQLFORM(db.messaging,fields=['subject','matter','filematter'])
    form.vars.toe=request.args[0]
    if form.accepts(request.vars,session):
        redirect(URL(r=request , f='companyprofileview',args=(request.args[1],request.args[2],request.args[3])))
    return dict(form=form)
    
def justforfun():
    form=SQLFORM.factory(
                            db.Field('te','string'),
                            db.Field('dropee',requires=IS_IN_SET(['Name','College','Work','CGPA','Company','highschool%','projects'])))
    if form.accepts(request.vars,session):
                                redirect(URL(r=request,f='checkrababu',args=[form.vars.te,form.vars.dropee]))
    return dict(form=form)

def checkrababu():
    a=request.args[1]
    if a=='Name' :redirect(URL(r=request , f='profile1checkname1',args=[request.args[0],request.args[1]] ))
    if a=='College' :redirect(URL(r=request , f='profile3college1',args=[request.args[0],request.args[1]] ))			
    if a=='Work' :redirect(URL(r=request , f='profile5pani1',args=[request.args[0],request.args[1]] ))			
    if a=='CGPA' :redirect(URL(r=request , f='profile3cgpa1' ,args=[request.args[0],request.args[1]]))			
    if a=='Company' :redirect(URL(r=request , f='companyworkedin1',args=[request.args[0],request.args[1]]))			
    if a=='highschool%' :redirect(URL(r=request , f='highschool1' ,args=[request.args[0],request.args[1]]))			
    if a=='projects' :redirect(URL(r=request , f='project1',args=[request.args[0],request.args[1]]))
       
    return dict()
def bar():
          form=[0]
          return dict(form=form) 
def profile1checkname2():
	data1=db(db.profile1.id>0).select()	
	data2=db(db.profile1.id>0).select()
	d4=[]
	d1=[]
	d2=[]
	d3={}
	d3['main']=request.args[0]
	for i in data1:
		if(re.search(request.args(0),i.first_name)):
			if d4.count(i.stid)==0:
				d1.append(i)
				d4.append(i.stid)
	for j in data2:
		if(re.search(request.args(0),j.last_name)):
			d2.append(j)
	return dict(d1=d1,d2=d2,d3=d3)


def profile3college2():
	data1=db(db.profile3.id>0).select()	
	d1=[]
	d2=[]
	d5=[]
	d3={}
	d3['main']=request.args[0]
	for i in data1:
		if(re.search(request.args(0),i.collegename)):
			if d5.count(i.stid)==0:
				d1.append(i)
				d5.append(i.stid)
	for j in d1:
		data2=db(db.profile1.stid==j.stid).select()
		d2.append(data2)
	return dict(d1=d1,d2=d2,d3=d3)

def profile5pani2():
	data1=db(db.profile5.id>0).select(orderby=db.profile5.id)	
	data2=db(db.profile5.id>0).select(db.profile5.id ,orderby=db.profile5.id)
	d1=[]
	d1=[]
	d2={}
	d3=[]
	d4=[]
	d5={}
	d6=[]
	d5['main']=request.args[0]
	for m in data1:
		if d1.count(m.id)==0:
			d1.append(m.id)
			d4.append(m)
	for i in d4:
		data3=db(db.profile5.stid==i.stid).select()
		count=0
		d2={}
		for k in data3:
			if k.pani:count=count+k.pani
		print count
		print request.args[0]
		if count > float(request.args[0] ):
			d3.append(i)
	return dict(d3=d3,d5=d5)
