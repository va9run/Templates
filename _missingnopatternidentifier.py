# Method 1:
import missingno as mno

def missing(col):
    df = df[col].isna()
    # Matrix gives heatmap can be replaced with bar or other
    mno.matrix(df) 

# Method 2:
    # Heatmap using plotly or Matplotlib 
import plotly.express as px 
def missingheat(col):
    df = df[col].isna()
    fig = px.imshow(df)
    fig.show()