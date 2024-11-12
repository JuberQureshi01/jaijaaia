from flask import Flask, flash, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, IntegerField, StringField,SelectField
from wtforms.validators import DataRequired,InputRequired

import regex
import pandas as pd
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Feludaisjatayu!'

class SequenceForm(FlaskForm):
	dna = TextAreaField('dna', validators=[ InputRequired()  ])
	#pattern = TextAreaField('pattern', validators=[ InputRequired()  ])
	pattern = SelectField('pattern', choices=[('NGG', 'NGA','NAG','YYG','TTN')  ]   )


	# simpleBool = BooleanField('simpleBool', default=False)
	
	
@app.route('/', methods=["GET", "POST"])
def sequence():
	form=SequenceForm()
	if request.method =='POST':
		print("print the sequence here :")
		print(form.dna.data)
		sequence=form.dna.data
		#sequence=form.dna.data
		pattern=form.pattern.data
		df1=pamsearch(pattern=pattern,sequence=sequence)
		print(df1)


		return render_template('result.html',tables=df1.to_html(),sequence=sequence,pattern=pattern)

	return render_template("index.html")


def pamsearch(pattern,sequence):
	pam=pattern.replace('N','[ACGT]').replace('R','[AG]').replace('Y','[CT]').replace('V','[ACG]')
	pam1 ='[ACGT]{20}'  +  pam
	NGG = regex.finditer(pam1, sequence,overlapped=True )
	ls=list()
	for match in NGG:
		laast=  'Sequence' +"\t" +str(match.start())+ "\t" + str(match.end()) + "\t" +str(match.group()) 
		ls.append(laast)
	#df1=pd.DataFrame(ls)
	df1=pd.DataFrame([x.split('\t') for x in ls])
	df1.columns=['Sr. No', 'Start','End','crRNAs']

	return (df1)
	

	


if __name__ == "__main__": 
 	app.run(debug=True)
