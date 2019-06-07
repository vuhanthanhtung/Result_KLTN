class query:
    def __init__(self, query, table_name, condition, option_query=None, option_condition=None, groupby=None, option_groupby=None, orderby=None, option_orderby=None):
        self.query = query
        self.table_name = table_name
        self.condition = condition
        self.option_query = option_query
        self.option_condition = option_condition
        self.groupby = groupby
        self.option_groupby = option_groupby
        self.orderby = orderby
        self.option_orderby = option_orderby
    def showQuery(self):
        print("Query:" ,self.query)
        print("Table:" ,self.table_name)
        print("condition:" ,self.condition)
        print("option_query:" ,self.option_query)
        print("option_condition:" ,self.option_condition)






#apt = query("select","lala","condition",None,"lele")
#apt.showQuery()

