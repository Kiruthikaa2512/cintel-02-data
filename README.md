# cintel-02-data
## Penguin Explorer – Dashboard by Kiruthikaa

This interactive dashboard is built using **Shiny for Python** and visualizes the **Palmer Penguins dataset**. Users can explore various biological measurements of penguins across different species using dynamic plots and filters.

### Features

* **Sidebar Controls**:

  * Select a numerical attribute to analyze
  * Adjust the number of bins for Plotly and Seaborn histograms
  * Filter by penguin species (Adelie, Gentoo, Chinstrap)

* **Main Content**:

  * Data Table (sortable, searchable)
  * Data Grid (alternative tabular view)
  * Plotly Histogram (interactive)
  * Seaborn Histogram (static)
  * Plotly Scatterplot (interactive, color-coded by species)

### Dataset

The application uses the [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/), which includes:

* Bill length and depth
* Flipper length
* Body mass
* Species and island information

This dataset is a modern alternative to the Iris dataset and is useful for demonstrating data visualization and interactivity.

### Technologies Used

* [Shiny for Python](https://shiny.posit.co/py/)
* [Plotly Express](https://plotly.com/python/)
* [Seaborn](https://seaborn.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Palmerpenguins Python Package](https://pypi.org/project/palmerpenguins/)
* [ShinyWidgets](https://shiny.posit.co/py/packages/shinywidgets/)

### Installation

To run the dashboard locally:

```bash
pip install shiny shinywidgets palmerpenguins plotly seaborn matplotlib
```

Then execute:

```bash
shiny run --reload app.py
```

Alternatively, it can be run directly in the [ShinyLive Playground](https://shinylive.io/py/) without local installation.

### Links

* Source Code: [GitHub Repository](https://github.com/Kiruthikaa2512/cintel-02-data)
* Dataset Documentation: [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/)
* Shiny for Python: [Documentation](https://shiny.posit.co/py/)
