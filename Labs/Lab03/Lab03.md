# GEOG-392/676 GIS Programming: Lab 03

>**Topic:** Python Read/Write Files and OOP
>
>**100 pt**
>

## Due Dates and Submission Instructions

> **where**: canvas link
>
> **when**: before next lab
>
> **what**: a PDF including all your code and results

## **Task:**

1. Learn how to read and write datasets files using Python.
2. Learn how to use Object-Oriented Programming to organize your code.

## **Load & View Datasets in GeoJson format**

`GeoJson` is a popular format for storing geospatial data. It is a `JSON` format for encoding a variety of geographic data structures. Storing data in `GeoJson` format is useful when you want to share your data with others or when you want to use it in a `GIS` application. Similar to the `shapefile` format, `GeoJson` is a container of features, and each feature has a geometry and a set of properties. The `geometry` is a GeoJSON object which represents a geographic feature's geometry, and the `properties` is a dictionary of additional information about the feature.

In this lab, you will load a `GeoJson` file containing census data for Brazos County, Texas, and view its contents. `GeoJson` file is located at: [Labs/Lab03/data/data.geojson](data/data.geojson)

### **Data Explaination**

This is a `vector` dataset containing the census tracts of `Brazos County`, `Texas`. The dataset includes the following information for each census tract:

- `GeoId`: The census tract's unique identifier.
- `ALAND`: The land area of the census tract in square meters.
- `AWATER`: The water area of the census tract in square meters.
- `Pop_Den`: The population density of the census tract in people per square kilometer.
- `Pop`: The total population of the census tract.
- `geometry`: The geometry of the census tract polygon.

### **Load Data Using `GeoPandas`**

Install `GeoPandas` library if you haven't done so already.

```bash
pip install geopandas
```

```python
import geopandas as gpd

# Load the GeoJson file into a GeoDataFrame
gdf = gpd.read_file('data/data.geojson')

```

### **View Data**

```python
# View the first 5 rows of the GeoDataFrame
print(gdf.head())
# view the column names
print(gdf.columns)
# view the shape of the GeoDataFrame
print(gdf.shape)
# view the data type of each column
print(gdf.dtypes)
```

## **Task 1. Finish the `CensusTract` Class Definition**

```python
class CensusTract:
    def __init__(self, geoid, population, geometry):
        self.geoid = geoid
        self.population = population
        self.geometry = geometry
    
    def calculate_population_density(self):
        # calculate the population density based on geometry
        ### >>>>>>>>>>>> YOUR CODE HERE <<<<<<<<<<< ###
        
        return population_density
        ### <<<<<<<<<<< END OF YOUR CODE <<<<<<<<<<< ###
```

**Hint**: The population density can be calculated by dividing the population by the area of the census tract. The area of the census tract can be calculated using the `GeoPandas` `area` attribute. `geometry` column of a `GeoDataFrame` is a `GeoSeries` of `shapely` objects, and the `area` attribute is a `float` of the area of the geometry in unit of the `CRS` of the `GeoDataFrame`. Documentation of `GeoSeries` can be found [here](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.html).

## Task 2. Calculate the Population Density for Each Census Tract

Now you have finished the `CensusTract` class, you can use it to calculate the population density for each census tract (each row of the original dataset). Then add the calculated population density to a new column in the `GeoDataFrame`.

```python
    # calculate the Population Density based on geometry
    ### >>>>>>>>>>>> YOUR CODE HERE <<<<<<<<<<< ###
    # instantiate the CensusTract class

    # calculate the population density for each census tract

    # create a new column for the population density

    ### <<<<<<<<<<< END OF YOUR CODE <<<<<<<<<<< ###

    # preview the data again
    print(gdf.head())
```

**Hints**:

- You can iterate over the rows of the `GeoDataFrame` using a for loop.
- Or you can use the `apply` and/or `lambda` function to apply the `calculate_population_density` method to each row of the `GeoDataFrame`.
- Locate column of a `GeoDataFrame` can be accessed using

    ```python
    <GeoDataFrame>[<column_name>]
    ```

- You can create a new column to the `GeoDataFrame` using

    ```python
    <GeoDataFrame>[<new_column_name>] = <new_column_values>
    ```

## Submission

Submit a PDF file containing your code and results.
Then `git commit` your code and `push` to your remote repository.

**Grading Rule:**

- 30 points for the `CensusTract` class definition.
- 30 points for the population density calculation.
- 20 points for the new column addition.
- 10 points for the code quality and docstring.
- 10 points for Github repository.

## Useful Links

- [GeoPandas Documentation](https://geopandas.org/en/stable/docs.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/reference/index.html#api)
- [Shapely Documentation](https://shapely.readthedocs.io/en/stable/manual.html)
- [Census Bureau County and County Equivalent Entities](https://www.census.gov/library/reference/code-lists/ansi.html#cou)
