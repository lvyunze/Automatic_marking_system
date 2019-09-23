# from docxtpl import DocxTemplate
# # import docxtpl
# #
# # tpl = DocxTemplate('test.docx')
# #
# # myimage = docxtpl.InlineImage(tpl,'标号.png')
# #
# #
# # tpl.save('test1.docx')

from docxtpl import DocxTemplate, InlineImage
# for height and width you have to use millimeters (Mm), inches or points(Pt) class :
from docx.shared import Mm, Inches, Pt
import jinja2
from jinja2.utils import Markup

tpl = DocxTemplate('test.docx')

context = {
    'myimage' : InlineImage(tpl,'标号.png',width=Mm(10)),
}
# testing that it works also when autoescape has been forced to True
jinja_env = jinja2.Environment(autoescape=True)
tpl.render(context, jinja_env)
tpl.save('test1.docx')