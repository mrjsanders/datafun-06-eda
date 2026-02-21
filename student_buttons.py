# student_buttons.py
import ipywidgets as widgets
from IPython.display import display, clear_output

def create_student_buttons(df, columns, create_boxplot_func):
    """
    Creates interactive buttons for each row in df to display individual boxplots.
    
    Parameters:
    - df : pandas DataFrame containing student data
    - columns : list of column names to include in the boxplot
    - create_boxplot_func : function to generate a boxplot for a given Series
    """
    buttons = []
    output = widgets.Output()

    for idx, row in df.iterrows():
        button = widgets.Button(
            description=f"Student {idx+1}",
            layout=widgets.Layout(width='100px')
        )
        buttons.append(button)

        # Closure to capture idx correctly
        def on_click_factory(student_idx):
            def on_click(b):
                with output:
                    clear_output(wait=True)
                    student_scores = df.loc[student_idx, columns]
                    create_boxplot_func(student_scores, title=f"Scores for Student {student_idx+1}")
            return on_click

        button.on_click(on_click_factory(idx))

    # Arrange buttons in two rows (adjust if needed)
    row1 = widgets.HBox(buttons[:9])
    row2 = widgets.HBox(buttons[9:])
    
    display(row1, row2, output)