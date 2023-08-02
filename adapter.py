from yf_api import choose_date
from displayGraph import DisplayGraph

def display_graph_for_ticker(ticker, start_date):
    df = choose_date(ticker, '01012020')
    if isinstance(df, str):
        print(df)
        return

    graph = DisplayGraph(df, start_date)
    graph.plot_data()
