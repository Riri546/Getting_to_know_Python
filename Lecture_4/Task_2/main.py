from telnetlib import SGA
import html_creater as hc
import xml_generstor as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

xg.new_create((dp.data_collection()))
