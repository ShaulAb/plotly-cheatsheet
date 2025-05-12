# Plotly Graph Selection Preferences

This document provides guidelines for selecting appropriate graph types in Plotly based on the types of variables to visualize.

## 1.  Key Variable Types

   * **Continuous Variable:** A variable that can take on any value within a range. (e.g., temperature, height, price).
   * **Discrete Variable:** A variable that can only take on specific, separate values. (e.g., category names, days of the week, counts).
   * **Time Series Variable:** A variable representing points in time.
   * **Spatial:** Data that includes geographic coordinates (latitude and longitude).

## 2.  Graph Selection by Variable Type

* **2.1 Time Series**

  * Use: Visualizing data points ordered over time.
  * Plotly Graph(s):
    * `Line plot` with time on the x-axis
    * `Bar plot` with time as the index

* **2.2 Two Continuous Variables**

  * Use: Showing the relationship between two quantitative measures.
  * Plotly Graph(s):
    * `Scatter plot`
    * `Density heatmap`

* **2.3 One Continuous and One Discrete Variable**

  * Use: Comparing a quantitative measure across different categories.
  * Plotly Graph(s):
    * `Histogram` appropriate for discrete variable with a maximum of 3 categories. in case of higher cardinality use `Box plot` or `Violin plot`
    * `Box plot` appropriate for discrete variable with a maximum of 7 categories. in case of higher cardinality collect the top 6 and the rest as "others"
    * `Violin plot` appropriate for discrete variable with a maximum of 7 categories. in case of higher cardinality collect the top 6 and the rest as "others"

* **2.4 Spatial Data (Latitude, Longitude)**

  * Use: Displaying data on a map.
  * Plotly Graph(s):
    * `Scatter plot` on a map
    * `Choropleth map` for showing values associated with geographic regions

* **2.5 One Continuous Variable**

  * Use: Showing the distribution of a single quantitative measure.
  * Plotly Graph(s):
    * `Histogram`
    * `Box plot` 
    * `Violin plot`

* **2.6 One Discrete Variable**

  * Use: Showing the distribution of a single categorical measure.
  * Plotly Graph(s):
    * `Histogram` appropriate for discrete variable with a maximum of 7 categories. in case of higher cardinality collect the top 6 and the rest as "others"
    * `Pie chart` appropriate for discrete variable with a maximum of 20 categories. in case of higher cardinality collect the top 19 and the rest as "others"

* **2.7 Two Discrete Variables**

  * Use: Showing the relationship between two categorical measures.
  * Plotly Graph(s):
    * `Count plot`
    * `Stacked bar chart`

* **2.8 Three or More Variables**

  * Use: Showing relationships between multiple variables.
  * Plotly Graph(s):
    * You can often use visual aesthetics (color, size, shape) in other plot types (e.g., scatter plot) to represent a third continuous or discrete variable
    * `3D Scatter Plot` (for three continuous variables)
    * `Contour plots` (for 2 continuous and one derived continuous variable)

* **2.9 Funnel (ordered steps)**

  * Use `px.funnel` for drop-off analysis across 3-8 ordered stages.  
  * Requires a tidy data-frame with *key* + *value* columns (value counts).

* **2.10 Hierarchy / Tree (two nested categoricals)**
    
  | Goal                           | Recommended plot              |
  |--------------------------------|-------------------------------|
  | Part-to-whole, space-efficient | `px.treemap`                  |
  | Storytelling radial            | `px.sunburst`                 |
  | Top-down flow                  | `px.icicle`                   |
  
  *Prefer shallow plots (≤ 3 variables) for readability.*

* **2.11 Flow diagrams (multi-dimensional paths)**

  * 4-6 numeric axes → `px.parallel_coordinates`  
  * Only / Mostly categorical axes → `px.parallel_categories` (bin numeric if needed)  
  * Order axes logically (time/importance → outcome) to expose patterns.

* **2.12 Multivariate / Multidimensional**  

  * Pairwise view → `px.scatter_matrix` (up to ~6 numeric dims)  
  * High-dimensional overview → `px.parallel_coordinates` with `color=` target metric.

3.  Example Code Snippets (Illustrative - Adapt to Your Data)**

```python
import plotly.express as px

# Time Series
fig = px.line(data, x="date", y="value", title="Time Series Plot")
fig.show()

# Two Continuous Variables
fig = px.scatter(data, x="var1", y="var2", title="Scatter Plot")
fig.show()

# One Continuous, One Discrete
fig = px.bar(data, x="category", y="value", title="Bar Chart")
fig.show()

# Spatial Data
fig = px.scatter_geo(data, lat="latitude", lon="longitude", title="Geospatial Plot")
fig.show()
```

## 4.  Limitations

   * **Data Size:** always plot a maximum of 10K data points, if the data is larger than that, use random sampling
   * **Cardinality:** for categorical variables, if the cardinality is too high, follow the guidelines above to ensure plot readability

