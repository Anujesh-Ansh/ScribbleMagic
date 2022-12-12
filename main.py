'''
Right now it is not working, as there is some error on the pywhatkit side
'''

import pywhatkit as pw

txt = "Hi hello, myself Anujesh Ansh, a student of Symbiosis Institute of Technology"

pw.text_to_handwriting(txt,"demo.png",(0,0,0))


print("End")