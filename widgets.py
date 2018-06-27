from datetime import date
from random import randint

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, row
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Button, CheckboxButtonGroup, CheckboxGroup, DataTable, DateFormatter, TableColumn, Dropdown, MultiSelect, RadioButtonGroup, RadioGroup, Select, Slider, RangeSlider, Panel, Tabs, TextInput, Toggle, Div, Paragraph

output_file("widgets.html")

button = Button(label="Foo", button_type="success")

checkbox_button_group = CheckboxButtonGroup( labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

checkbox_group = CheckboxGroup( labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

data = dict( dates=[date(2014, 3, i+1) for i in range(10)], downloads=[randint(0, 100) for i in range(10)],)
source = ColumnDataSource(data)
columns = [ TableColumn(field="dates", title="Date", formatter=DateFormatter()), TableColumn(field="downloads", title="Downloads"), ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)

multi_select = MultiSelect(title="Option:", value=["foo", "quux"], options=[("foo", "Foo"), ("bar", "BAR"), ("baz", "bAz"), ("quux", "quux")])

radio_button_group = RadioButtonGroup( labels=["Option 1", "Option 2", "Option 3"], active=0)

radio_group = RadioGroup( labels=["Option 1", "Option 2", "Option 3"], active=0)

select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])

slider = Slider(start=0, end=10, value=1, step=.1, title="Slider", bar_color="blue")

range_slider = RangeSlider(start=0, end=10, value=(1,9), step=.1, title="RangeSlider")

tp = figure(plot_width=300, plot_height=300)
tp.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="green", alpha=0.5)
panel = Tabs(tabs=[Panel(child=tp, title="Panel")])
#panel = Panel(child=tp, title="Panel") #doesn't work

p1 = figure(plot_width=300, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="circle")
p2 = figure(plot_width=300, plot_height=300)
p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="line")
tabs = Tabs(tabs=[ tab1, tab2])

text_input = TextInput(value="default", title="Label:")

toggle = Toggle(label="Foo", button_type="success")

div = Div(text="""Your <a href="https://en.wikipedia.org/wiki/HTML">HTML</a>-supported text is initialized with the <b>text</b> argument.  The
remaining div arguments are <b>width</b> and <b>height</b>. For this example, those values
are <i>200</i> and <i>100</i> respectively.""",
width=200, height=100)

p = Paragraph(text="""Your text is initialized with the 'text' argument.  The
remaining Paragraph arguments are 'width' and 'height'. For this example, those values
are 200 and 100 respectively.""",
width=200, height=100)

show(widgetbox([button, checkbox_button_group, checkbox_group, data_table, dropdown, multi_select, radio_button_group, radio_group, select, slider, range_slider, panel, tabs, text_input, toggle, div, p]))
