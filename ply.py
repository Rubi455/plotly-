import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
file_path = r"C:\Users\rubik\Desktop\python\hr"
if not os.path.exists(file_path):
    print("Error: File not found. Please check the file path.")
else:
    print("File found. Loading data...")
    data = pd.read_csv(file_path)
    print("Dataset Info:")
    print(data.info())  
    print("\nDataset Preview:")
    print(data.head()) 
    columns_of_interest = ['Cycle', 'Re', 'Rct']  
    if not all(col in data.columns for col in columns_of_interest):
        print("Error: Missing required columns. Check the column names in your dataset.")
    else:
        filtered_data = data[columns_of_interest]
        filtered_data = filtered_data.dropna()

        print("\nFiltered Data:")
        print(filtered_data.head())  
        fig_re = px.line(
            filtered_data,
            x='Cycle',
            y='Re',
            title='Electrolyte Resistance (Re) Over Charge/Discharge Cycles',
            labels={'Cycle': 'Charge/Discharge Cycle', 'Re': 'Electrolyte Resistance (Ohms)'},
            template='plotly'
        )
        fig_re.show()
        fig_rct = px.line(
            filtered_data,
            x='Cycle',
            y='Rct',
            title='Charge Transfer Resistance (Rct) Over Charge/Discharge Cycles',
            labels={'Cycle': 'Charge/Discharge Cycle', 'Rct': 'Charge Transfer Resistance (Ohms)'},
            template='plotly'
        )
        fig_rct.show()
        fig_combined = go.Figure()
        fig_combined.add_trace(go.Scatter(
            x=filtered_data['Cycle'],
            y=filtered_data['Re'],
            mode='lines',
            name='Re (Electrolyte Resistance)'
        ))
        fig_combined.add_trace(go.Scatter(
            x=filtered_data['Cycle'],
            y=filtered_data['Rct'],
            mode='lines',
            name='Rct (Charge Transfer Resistance)'
        ))
        fig_combined.update_layout(
            title='Battery Resistance Parameters Over Charge/Discharge Cycles',
            xaxis_title='Charge/Discharge Cycle',
            yaxis_title='Resistance (Ohms)',
            legend_title='Resistance Type',
            template='plotly'
        )
        fig_combined.show()
