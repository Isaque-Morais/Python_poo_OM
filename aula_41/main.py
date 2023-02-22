from classes import Writer
from classes import Pen
from classes import Typewriter

writer = Writer('Isaque')
pen = Pen('Bic')
typewriter = Typewriter()

writer.tool = pen
writer.tool.write()