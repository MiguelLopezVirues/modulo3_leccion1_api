# 📊 Foursquare Project - Location Insights and Analytics

<div style="text-align: center;">
  <img src="assets/foursquare.jpg" alt="project-cover" />
</div>

## 📝 Project Overview

This project analyzes location-based data from Foursquare to identify venues useful to a business. In this case, a film production company is going to produce a reality TV Show where friends prank another friend, after drinks, and scare him to death simulating paranormal or unnatural events. , and provide insights for improving urban planning and business decision-making.

The exploration covers making requests venue distribution across various categories, user behavior trends, and how external factors such as seasonality influence visitation patterns.

Key objectives:

1. Understanding venue popularity and distribution across different areas.
2. Identifying opportunities for business and infrastructure development.

## 📁 Project Structure

```bash
Foursquare-Location-Insights/
├── data/                # Processed data
│   ├── city_coordinates.csv
│   └── general_categories.csv
├── notebooks/           # Jupyter notebook with the process
│   └── lab1_apis.ipynb
├── src/                 # Data processing and utility scripts
│   └── support_lab1_api.py
├── Pipfile              # Dependency management file
├── Pipfile.lock         # Lockfile for exact versions of dependencies
└── README.md            # Project documentation (this file)
```

## 🛠️ Installation and Requirements

To run this project, you will need the following tools and libraries:

- Python 3.8+
- pandas
- numpy
- geopy
- foursquare API

**Documentation Links:**
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)  
- [pandas Documentation](https://pandas.pydata.org/)  
- [NumPy Documentation](https://numpy.org/)  
- [Geopy Documentation](https://geopy.readthedocs.io/en/stable/)
- [Foursquare API Documentation](https://developer.foursquare.com/)

#### Setting up the Environment with Pipenv

Clone this repository by running the following commands:
```bash
git clone https://github.com/MiguelLopezVirues/modulo3_leccion1_api
```

To replicate the project's environment, use Pipenv with the included ``Pipfile.lock``:
```bash
pipenv install
pipenv shell  
```

Alternatively, install the dependencies from ``requirements.txt``:
```bash
pip install -r requirements.txt  
```

## 📊 Results and Conclusions

For detailed results, please check the ``data_analysis.ipynb`` notebook, which contains the process of extracting the information.

## 🔄 Next Steps

- Refine venue clustering methods to enhance location-based recommendations.

## 🤝 Contributions

Contributions are welcome! Feel free to open a pull request or an issue for any suggestions or improvements.

## ✒️ Authors

Miguel López Virués - [GitHub Profile](https://github.com/miguellopezvirues)  

## 📜 License

This project is licensed under the MIT License.
