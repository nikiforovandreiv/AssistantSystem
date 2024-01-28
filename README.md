# Used Cars Price Prediction PyQt6 Application 

**Authors:**
- Nikiforov Andrei (Student ID: 22211653)
- Mikita Zyhmantovich (Student ID: 22210475)

**Project Repository:**
[https://mygit.th-deg.de/an17653/sas-project-2](https://mygit.th-deg.de/an17653/sas-project-2)

**Project Wiki:**
[https://mygit.th-deg.de/an17653/sas-project-2/-/wikis/home](https://mygit.th-deg.de/an17653/sas-project-2/-/wikis/home)

## Project Description

Welcome to our PyQt6 Car Price Prediction App!

Have you ever wondered about the fair market value of a used car? 
Our Car Price Prediction App is here to assist you in estimating the price of a vehicle based on various input features. 
This user-friendly application utilizes PyQt6 for its sleek graphical interface, 
allowing you to effortlessly input information and obtain a predicted price.

### Key Features:

- **Intuitive Input Interface:**
  - Easily input nine essential features of the car:
    - Year 
    - Mileage
    - Tax
    - MPG (Miles Per Gallon)
    - Engine Size
    - Brand
    - Model
    - Fuel Type
    - Transmission Type
    
- **Real-time Prediction:**
  - Our application employs a powerful regression model to provide you with a real-time prediction of the car's estimated price. 
  - Gain insights into the potential value of your vehicle or one you're interested in.

- **Graphical Analysis:**
  - Explore the relationships between different variables and the predicted price through interactive scatter plots. 
  - Visualize how each feature influences the overall estimated price.

- **Data Insights:**
  - The app performs a comprehensive analysis of the provided dataset using a regressor model. 
  - Uncover hidden patterns and trends in the data, empowering you with valuable information for decision-making.

- **User-Friendly Design:**
  - Designed with the end-user in mind, our application offers a clean and intuitive interface. 
  - Input data effortlessly and navigate through insightful visualizations with ease.

- **Customization Options:**
  - Tailor your experience by adjusting input parameters and exploring how changes impact the predicted price. 
  - Experiment with different scenarios to better understand the factors influencing car prices.
  - 
- **Informative Metrics:**
  - Get additional insights into the dataset, including summary statistics 
  - Allowing you to better comprehend the distribution and characteristics of the provided data.

- **Responsive Graphs:**
  - Experience dynamic and responsive scatter plots that update in real-time as you modify input values. 
  - See the predicted price adapt instantly to changes in the features.

- **Educational Value:**
  - Learn more about the factors affecting car prices as you interact with the app. 
  - Gain valuable knowledge about the relationships between different variables and their impact on the final estimation.

Whether you're a car enthusiast, a prospective buyer, or simply curious about the fascinating world of predictive modeling, 
our Car Price Prediction App is a valuable tool for anyone seeking accurate and data-driven insights into used car pricing. 
Download and explore the future of car valuation today!

## Prerequisites

**Project Prerequisites:**
[https://mygit.th-deg.de/an17653/sas-project-2/-/blob/main/requirements.txt](https://mygit.th-deg.de/an17653/sas-project-2/-/blob/main/requirements.txt)

### 

### joblib~=1.3.2:
- **Description:** 
  - Joblib is a set of tools to provide lightweight pipelining in Python. 
  - It provides utilities for parallel computing, particularly in the context of data science and machine learning.
- **Version Specification:**
  - This project requires Joblib version 1.3.2.

### pandas~=2.1.4:
- **Description:** 
  - Pandas is a powerful and easy-to-use data manipulation and analysis library for Python. 
  - It provides data structures like DataFrame for efficient data manipulation.
- **Version Specification:** 
  - This project requires Pandas version 2.1.4.

### seaborn~=0.13.1:
- **Description:** 
  - Seaborn is a statistical data visualization library based on Matplotlib. 
  - It provides a high-level interface for drawing attractive and informative statistical graphics.
- **Version Specification:** 
  - This project requires Seaborn version 0.13.1.

### PyQt6~=6.6.1:
- **Description:** 
  - PyQt is a set of Python bindings for Qt libraries. 
  - PyQt6 is the latest version, providing a set of Python modules to enable the use of Qt6 in Python applications.
- **Version Specification:** 
  - This project requires PyQt6 version 6.6.1.

### matplotlib~=3.8.2:
- **Description:** 
  - Matplotlib is a 2D plotting library for Python. 
  - It produces publication-quality figures in a variety of formats and interactive environments across platforms.
- **Version Specification:** 
  - This project requires Matplotlib version 3.8.2.

### scikit-learn~=1.3.2:
- **Description:** 
  - Scikit-learn is a machine learning library for Python. 
  - It provides simple and efficient tools for data mining and data analysis, built on NumPy, SciPy, and Matplotlib.
- **Version Specification:** 
  - This project requires scikit-learn version 1.3.2.

## Installation

### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Python >= 3.6 and <= 3.10
- pip (Python package installer)
- Virtualenv (optional but recommended)

### 1. Clone the Repository
First, clone the project repository to your local machine using the following command:
```bash
git clone https://mygit.th-deg.de/an17653/sas-project-2.git
cd sas-project-2
```

### 2. Create a Virtual Environment (Optional)
Creating a virtual environment is a good practice to isolate your project dependencies. 
To create a virtual environment, run the following commands:
```bash
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On Linux/macOS
source venv/bin/activate
```

### 3. Install Required Modules
Navigate to the project directory and install the necessary Python modules by running:
```bash
pip install -r requirements.txt
```
This command will install all the dependencies listed in the requirements.txt file, 
ensuring that your environment is set up correctly for the application.

### 4. Start the Application
After installing the required modules, start the application by running:
```bash
python main.py
```
This command will launch the Car Price Prediction App. 
Explore its features and enjoy predicting car prices! 
If you encounter any issues during installation or execution, 
please refer to the troubleshooting section or contact our support team.

## Basic Usage

Start the application by running:
```bash
python main.py
```

By the start of your application you would be able to observe:
- Top Model
- Average Mileage
- Average MPG

As well as seeing 1 graph with options of:
- Year vs. Price
- Mileage vs. Price
- Tax vs. Price
- MPG vs. Price
- Engine Size vs. Price

We can select values of:
- Brand
- Model
- Fuel Type
- MPG(1-500)
- Tax(1-1000)
- Year Of Production(2000-2024)
- Trasmission

We can type values of:
- Mileage
- Engine Size

Also, the main function would be uploading your own csv file and train the model using that csv file.
All you have to do is press **File** menu button -> **Import CSV File** upload button and then choose your own csv file.

After all the values have been set and csv uploaded and trained, you have to press the **Predict Price** button. 
Then the predicted price of the car will be displayed, as well as the graphs will update with the predicted point.

## Implementation of the Requests

### Requests:
1) Desktop App with PyQT6 has to be developed.
2) A requirements.txt file must be used to list the used Python modules.
3) A README.md file must be created with the structure described in part 01.
4) The module venv must be used.
5) A free data source must be used. You may find it for example at Kaggle, SciKit (but not the built-in
ones), or other.
6) There must be a data import (predefined format and content of CSV).
7) The data must be read from a file after clicking on a (menu) button or directly after starting the app.
8) The data must be analyzed with Pandas methods, so that a user gets on overview.
9) You may use the functions dataframe.info(), dataframe.describe() and/or dataframe.corr()
for that.
10) You may also use other metrics or diagrams to do this.
11) Create several input widgets (at least 3, where 2 must be different) that change some feature variables.
12) A Scikit training model algorithm (e.g. from Aurélien Géron, Chapter 4) must be applied.
13) Create 1 or 2 output canvas, i.e. for data visualization
14) At least 3 statistical metrics over the input data must be shown
15) The app must react interactively to the change of input parameter with a new prediction with visualization.

### Implementation:

1) Desktop App with PyQT6 has been developed.
2) A requirements.txt file is used to list the used Python modules.
3) A README.md file is created with the structure described in part 01.
4) The module venv has been used.
5) A free data source has been used.
6) There is a data import (predefined format and content of CSV):
    ```
    # Lines 238 - 252 in main.py
    # Create a menu bar
    menubar = self.menuBar()
    
    # Create a File menu
    file_menu = menubar.addMenu("File")
    
    # Create "Import CSV File" action
    import_csv_file_action = QAction("Import CSV File", self)
    # Set icon for the action
    import_csv_file_img_path = os.path.join(os.path.dirname(__file__), 'img/import_csv_file_action_img.png')
    import_csv_file_action.setIcon(QIcon(import_csv_file_img_path))
    # Connect Import CSV File action signal to a custom slot
    import_csv_file_action.triggered.connect(self.import_csv_file)
    # Add open action to file_menu
    file_menu.addAction(import_csv_file_action)
    ```
7) The data is read from a file after clicking on a (menu) button and directly after starting the app.
    ```    
    # Lines 1210 - 1228 in main.py
    def import_csv_file(self):
    file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV file", "", "CSV File (*.csv)")
    
    if file_path:
        # Read the CSV file into a DataFrame using pandas
        self.df = pd.read_csv(file_path)
        print("File chosen and loaded into variable.")
    
        # Load the saved random forest model
        self.update_plot()
        # Analyze the input DataFrame
        self.df_analyze = DFAnalyze(self.df).analyze()
        self.df = DFPreprocess(self.df).preprocess()
        self.df = self.df.dropna()
        df_train = DFTrain(self.df)
        self.random_forest_model = df_train.train_random_forest_regressor()
        df_train.save_trained_model()
    else:
        print("No file chosen.")
    ```
8) The data is analyzed with Pandas methods, so that a user gets on overview.
    ```
    # Lines 112 - 113 in main.py
    # df_analyze.py is responsible for it
    # Analyze the input DataFrame
    self.df_analyze = DFAnalyze(df).analyze()
    ```
9) The functions dataframe.info(), dataframe.describe() and/or dataframe.corr() have been used.
    ```
    # Lines 27 - 29 in df_analyze.py
    # Print basic information about the DataFrame
    print(f"\n{self.text_format.BOLD}DataFrame Info:{self.text_format.RESET}\n")
    print(self.df.info())
    
    # Lines 41 - 43 in df_analyze.py
    # Print summary statistics
    print(f"\n{self.text_format.BOLD}Summary Statistics:{self.text_format.RESET}\n")
    print(self.df.describe())
    ```
10) Other metrics and diagrams to do this have been used.
    ```
    # Lines 112 - 113 in main.py
    # df_analyze.py is responsible for it
    # Analyze the input DataFrame
    self.df_analyze = DFAnalyze(df).analyze()
    ```
11) Several input widgets (at least 3, where 2 must be different) that change some feature variables have been created.
    ```
    # In total there are 8 input widgets
    # They are created in main.py -> setup_ui()
    ```
12) A Scikit training model algorithm (e.g. from Aurélien Géron, Chapter 4) has been applied.
    ```
    # df_train.py is responsible for it
    # Random Forest has been used
    ```
13) 1 output canvas for data visualization has been created.
    ```
    # Lines 651 - 682 in main.py
    # Create car price graphics view
    self.carPriceGraphicsView = QWidget(self)
    self.carPriceGraphicsView.setObjectName(u"carPriceGraphicsView")
    self.carPriceGraphicsView.setObjectName(u"carPriceGraphicsView")
    self.carPriceGraphicsView.setGeometry(QRect(200, 60, 571, 361))

    self.scatterMainLayout = QVBoxLayout(self.carPriceGraphicsView)

    # Select 100 random rows from your DataFrame
    self.random_sample_df = self.df.sample(n=100, random_state=42)

    # Create a scatter plot for year vs. price
    self.scatter_fig, ax = plt.subplots()
    self.scatter_plot = sns.scatterplot(data=self.random_sample_df, y="price", x="year", ax=ax)
    self.scatter_plot.set_title("Scatter Plot: Price vs. Year")

    # Customize xlabel and ylabel appearance
    self.scatter_plot.set_xlabel("Year", fontsize=12, labelpad=5)
    self.scatter_plot.set_ylabel("Price", fontsize=12, labelpad=5)

    self.scatter_canvas = FigureCanvasQTAgg(self.scatter_fig)

    self.scatter_layout = QVBoxLayout()
    self.scatter_layout.addWidget(self.scatter_canvas)

    self.scatter_fig.tight_layout(pad=2)

    # Add a toolbar to the scatter canvas
    self.toolbar = NavigationToolbar2QT(self.scatter_canvas, self)
    self.scatterMainLayout.addWidget(self.toolbar)

    self.scatterMainLayout.addLayout(self.scatter_layout)
    ```
14) 3 statistical metrics over the input data are shown
    ```
    # Lines 687 - 766 in main.py
    # Create metrics main layout
    self.metricsMainLayout = QWidget(self)
    self.metricsMainLayout.setObjectName(u"verticalLayoutWidget_2")
    self.metricsMainLayout.setGeometry(QRect(489, 429, 281, 45))

    # Create metrics vertical layout
    self.metricsVerticalLayout = QVBoxLayout(self.metricsMainLayout)
    self.metricsVerticalLayout.setSpacing(0)
    self.metricsVerticalLayout.setObjectName(u"metricsVerticalLayout")
    self.metricsVerticalLayout.setContentsMargins(0, 0, 0, 0)

    # Create metrics horizontal layout
    self.metricsHorizontalLayout = QHBoxLayout()
    self.metricsHorizontalLayout.setSpacing(0)
    self.metricsHorizontalLayout.setObjectName(u"metricsHorizontalLayout")

    # Create top model label
    self.topModelLabel = QLabel(self.metricsMainLayout)
    self.topModelLabel.setObjectName(u"topModelLabel")
    self.topModelLabel.setFont(default_label_font)
    self.topModelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add top model label to metrics horizontal layout
    self.metricsHorizontalLayout.addWidget(self.topModelLabel)

    # Create avg mileage label
    self.avgMileageLabel = QLabel(self.metricsMainLayout)
    self.avgMileageLabel.setObjectName(u"avgMileageLabel")
    self.avgMileageLabel.setFont(default_label_font)
    self.avgMileageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add avg mileage label to metrics horizontal layout
    self.metricsHorizontalLayout.addWidget(self.avgMileageLabel)

    # Create avg mpg label
    self.avgMPGLabel = QLabel(self.metricsMainLayout)
    self.avgMPGLabel.setObjectName(u"avgMPGLabel")
    self.avgMPGLabel.setFont(default_label_font)
    self.avgMPGLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add avg mpg label to metrics horizontal layout
    self.metricsHorizontalLayout.addWidget(self.avgMPGLabel)

    # Add metrics horizontal layout to metrics vertical layout
    self.metricsVerticalLayout.addLayout(self.metricsHorizontalLayout)

    # Create metrics horizontal layout 2
    self.metricsHorizontalLayout_2 = QHBoxLayout()
    self.metricsHorizontalLayout_2.setSpacing(0)
    self.metricsHorizontalLayout_2.setObjectName(u"metricsHorizontalLayout_2")

    # Create top model result label
    self.topModelResultLabel = QLabel(self.metricsMainLayout)
    self.topModelResultLabel.setObjectName(u"topModelResultLabel")
    self.topModelResultLabel.setFont(default_label_font)
    self.topModelResultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add top model result label to metrics horizontal layout 2
    self.metricsHorizontalLayout_2.addWidget(self.topModelResultLabel)

    # Create avg mileage result label
    self.avgMileageResultLabel = QLabel(self.metricsMainLayout)
    self.avgMileageResultLabel.setObjectName(u"avgMileageResultLabel")
    self.avgMileageResultLabel.setFont(default_label_font)
    self.avgMileageResultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add avg mileage result label to metrics horizontal layout 2
    self.metricsHorizontalLayout_2.addWidget(self.avgMileageResultLabel)

    # Create avg mpg result label
    self.avgMPGResultLabel = QLabel(self.metricsMainLayout)
    self.avgMPGResultLabel.setObjectName(u"avgMPGResultLabel")
    self.avgMPGResultLabel.setFont(default_label_font)
    self.avgMPGResultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add top model result label to metrics horizontal layout 2
    self.metricsHorizontalLayout_2.addWidget(self.avgMPGResultLabel)

    # Add metrics horizontal layout 2 to metrics vertical layout
    self.metricsVerticalLayout.addLayout(self.metricsHorizontalLayout_2)
    ```
15) The app reacts interactively to the change of input parameter with a new prediction with visualization.
    ```
    # The app reacts interactively to the change of input parameter 
    # with a new prediction with visualization when 'Pridect Price' button is pressed.
    ```

## Work Done

Nikiforov Andrei:
- Graphical User Interface
- Pandas with Numpy

Mikita Zyhmantovich:
- Visualization
- Scikit-Learn

Both:
- General Python Programming

We helped each other during the whole project with our respective parts, 
discussed Implementation and implemented it together.