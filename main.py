import os
import sys

import joblib
import pandas as pd
import seaborn as sns

from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PyQt6.QtGui import (QBrush, QColor, QFont, QPalette, QIntValidator, QAction, QIcon, QValidator)
from PyQt6.QtWidgets import (QApplication, QComboBox, QDial, QMainWindow,
                             QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QRadioButton, QSlider,
                             QVBoxLayout, QWidget, QSizePolicy, QFileDialog)

from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT

from df_analyze import DFAnalyze
from df_preprocess import DFPreprocess
from df_train import DFTrain


class CustomValidator(QValidator):
    def validate(self, input_str, pos):
        try:
            value = float(input_str)
            if 0.0 <= value <= 10.0 and len(input_str) <= 3:
                return QValidator.State.Acceptable, input_str, pos
            else:
                return QValidator.State.Invalid, input_str, pos
        except ValueError:
            if input_str == '':
                return QValidator.State.Acceptable, input_str, pos
            return QValidator.State.Invalid, input_str, pos


class UICarPricePredictionDialog(QMainWindow):
    def __init__(self, df):
        super().__init__()

        # Load various machine learning, scaler and label encoder models

        # Load the saved random forest model
        self.random_forest_model_filename = 'random_forest_regressor_model.joblib'
        self.random_forest_model = joblib.load('default_model/' + self.random_forest_model_filename)

        # Load the brand scaler model
        self.brand_scaler_model_filename = 'brand_scaler_model.joblib'
        self.brand_scaler_model = joblib.load('default_model/scaler/' + self.brand_scaler_model_filename)

        # Load the model scaler model
        self.model_scaler_model_filename = 'model_scaler_model.joblib'
        self.loaded_model_scaler_model = joblib.load('default_model/scaler/' + self.model_scaler_model_filename)

        # Load the year scaler model
        self.year_scaler_model_filename = 'year_scaler_model.joblib'
        self.year_scaler_model = joblib.load('default_model/scaler/' + self.year_scaler_model_filename)

        # Load the transmission scaler model
        self.transmission_scaler_model_filename = 'transmission_scaler_model.joblib'
        self.transmission_scaler_model = joblib.load('default_model/scaler/' + self.transmission_scaler_model_filename)

        # Load the mileage scaler model
        self.mileage_scaler_model_filename = 'mileage_scaler_model.joblib'
        self.mileage_scaler_model = joblib.load('default_model/scaler/' + self.mileage_scaler_model_filename)

        # Load the fuelType scaler model
        self.fuelType_scaler_model_filename = 'fuelType_scaler_model.joblib'
        self.fuelType_scaler_model = joblib.load('default_model/scaler/' + self.fuelType_scaler_model_filename)

        # Load the tax scaler model
        self.tax_scaler_model_filename = 'tax_scaler_model.joblib'
        self.tax_scaler_model = joblib.load('default_model/scaler/' + self.tax_scaler_model_filename)

        # Load the mpg scaler model
        self.mpg_scaler_model_filename = 'mpg_scaler_model.joblib'
        self.mpg_scaler_model = joblib.load('default_model/scaler/' + self.mpg_scaler_model_filename)

        # Load the engineSize scaler model
        self.engineSize_scaler_model_filename = 'engineSize_scaler_model.joblib'
        self.engineSize_scaler_model = joblib.load('default_model/scaler/' + self.engineSize_scaler_model_filename)

        # Load the brand label encoder model
        self.brand_label_encoder_model_filename = 'brand_label_encoder_model.joblib'
        self.brand_label_encoder = joblib.load('default_model/label_encoder/' + self.brand_label_encoder_model_filename)

        # Load the model label encoder model
        self.model_label_encoder_model_filename = 'model_label_encoder_model.joblib'
        self.model_label_encoder = joblib.load('default_model/label_encoder/' + self.model_label_encoder_model_filename)

        # Load the transmission label encoder model
        self.transmission_label_encoder_model_filename = 'transmission_label_encoder_model.joblib'
        self.transmission_label_encoder = joblib.load(
            'default_model/label_encoder/' + self.transmission_label_encoder_model_filename)

        # Load the fuel type label encoder model
        self.fuelType_label_encoder_model_filename = 'fuelType_label_encoder_model.joblib'
        self.fuelType_label_encoder = joblib.load(
            'default_model/label_encoder/' + self.fuelType_label_encoder_model_filename)

        # Initialize variables and UI elements

        # Placeholder for a DataFrame for random samples
        self.random_sample_df = None

        # Placeholder for a DataFrame for random samples
        self.numeric_columns = ["year", "mileage", "tax", "mpg", "engineSize"]

        # Index to track the current variable being displayed
        self.current_variable_index = 0

        # Analyze the input DataFrame
        self.df_analyze = DFAnalyze(df).analyze()

        # Preprocess the input DataFrame by removing outliers
        self.df = DFPreprocess(df).remove_outliers()

        # Set object name for the dialog (if not already set)
        if not self.objectName():
            self.setObjectName(u"carPricePredictionDialog")

        # Resize the dialog to a default size of 800x600
        self.resize(800, 600)

        # Initialize UI elements (layout, labels, buttons, etc.)
        # Note: These elements are currently set to None and will be assigned during setup_ui()
        self.optionsMainLayout = None
        self.optionsVerticalLayout = None
        self.brandVerticalLayout = None
        self.brandLabel = None
        self.brandComboBox = None
        self.modelVerticalLayout = None
        self.modelLabel = None
        self.modelComboBox = None
        self.fuelTypeVerticalLayout = None
        self.fuelTypeLabel = None
        self.fuelTypeComboBox = None
        self.mileageVerticalLayout = None
        self.mileageLabel = None
        self.mileageLineEdit = None
        self.engineSizeVerticalLayout = None
        self.engineSizeLabel = None
        self.engineSizeLineEdit = None
        self.mpgMainLayout = None
        self.mpgVerticalLayout = None
        self.mpgLabel = None
        self.mpgDial = None
        self.mpgNumberLabel = None
        self.taxMainLayout = None
        self.taxVerticalLayout = None
        self.taxLabel = None
        self.taxDial = None
        self.taxNumberLabel = None
        self.yearMainLayout = None
        self.yearVerticalLayout = None
        self.yearHorizontalLayout = None
        self.yearLabel = None
        self.yearNumberLabel = None
        self.yearSlider = None
        self.transmissionMainLayout = None
        self.transmissionHorizontalLayout = None
        self.transmissionLabel = None
        self.transmissionHorizontalLayout_2 = None
        self.manualRadioButton = None
        self.autoRadioButton = None
        self.semiAutoRadioButton = None
        self.otherRadioButton = None
        self.switchVariableLabel = None
        self.lastVariableButton = None
        self.nextVariableButton = None
        self.currentVariableLabel = None
        self.currentVariableResultLabel = None
        self.carPriceGraphicsView = None
        self.scatterMainLayout = None
        self.scatter_fig = None
        self.scatter_plot = None
        self.scatter_canvas = None
        self.scatter_layout = None
        self.metricsMainLayout = None
        self.metricsVerticalLayout = None
        self.metricsHorizontalLayout = None
        self.topModelLabel = None
        self.avgMileageLabel = None
        self.avgMPGLabel = None
        self.metricsHorizontalLayout_2 = None
        self.topModelResultLabel = None
        self.avgMileageResultLabel = None
        self.avgMPGResultLabel = None
        self.predictedPriceMainLayout = None
        self.predictedPriceHorizontalLayout = None
        self.predictedPriceLabel = None
        self.predictedPriceNumberLabel = None
        self.mpgDescription = None
        self.taxDescription = None
        self.predictPriceButton = None
        self.predicted_price = None
        self.toolbar = None

        # Setup UI elements
        self.setup_ui()

        # Update statistics
        self.update_stats()

    def setup_ui(self):
        # Set color palette
        palette = self.palette()
        brush = QBrush(QColor(20, 0, 81, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 255, 196, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(170, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        brush3 = QBrush(QColor(149, 237, 255, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush3)
        self.setPalette(palette)

        # Set default label font
        default_label_font = QFont()
        default_label_font.setPointSize(12)

        # Set default description font
        default_description_font = QFont()
        default_description_font.setPointSize(9)
        default_description_font.setItalic(True)

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

        # Create options main vertical layout
        self.optionsMainLayout = QWidget(self)
        self.optionsMainLayout.setObjectName(u"verticalLayoutWidget")
        self.optionsMainLayout.setGeometry(QRect(30, 30, 160, 301))

        # Create options vertical layout
        self.optionsVerticalLayout = QVBoxLayout(self.optionsMainLayout)
        self.optionsVerticalLayout.setSpacing(10)
        self.optionsVerticalLayout.setObjectName(u"optionsVerticalLayout")
        self.optionsVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # Create brand vertical layout
        self.brandVerticalLayout = QVBoxLayout()
        self.brandVerticalLayout.setSpacing(0)
        self.brandVerticalLayout.setObjectName(u"brandVerticalLayout")

        # Create brand label
        self.brandLabel = QLabel(self.optionsMainLayout)
        self.brandLabel.setObjectName(u"brandLabel")
        self.brandLabel.setFont(default_label_font)

        # Add brand label to brand vertical layout
        self.brandVerticalLayout.addWidget(self.brandLabel)

        # Create brand combobox
        self.brandComboBox = QComboBox(self.optionsMainLayout)
        self.brandComboBox.addItem("")
        self.brandComboBox.addItem("")
        self.brandComboBox.addItem("")
        self.brandComboBox.addItem("")
        self.brandComboBox.setObjectName(u"brandComboBox")
        self.brandComboBox.setFont(default_label_font)
        self.brandComboBox.setMouseTracking(False)
        self.brandComboBox.setMaxVisibleItems(4)

        # Add brand combobox to brand vertical layout
        self.brandVerticalLayout.addWidget(self.brandComboBox)

        # Add brand vertical layout to options vertical layout
        self.optionsVerticalLayout.addLayout(self.brandVerticalLayout)

        # Create model vertical layout
        self.modelVerticalLayout = QVBoxLayout()
        self.modelVerticalLayout.setSpacing(0)
        self.modelVerticalLayout.setObjectName(u"modelVerticalLayout")

        # Create model label
        self.modelLabel = QLabel(self.optionsMainLayout)
        self.modelLabel.setObjectName(u"modelLabel")
        self.modelLabel.setFont(default_label_font)

        # Add model label to model vertical layout
        self.modelVerticalLayout.addWidget(self.modelLabel)

        # Create model combobox
        self.modelComboBox = QComboBox(self.optionsMainLayout)
        for i in range(91):
            self.modelComboBox.addItem("")
        self.modelComboBox.setObjectName(u"modelComboBox")
        self.modelComboBox.setFont(default_label_font)
        self.modelComboBox.setMouseTracking(False)
        self.modelComboBox.setMaxVisibleItems(4)

        # Add model combobox to model vertical layout
        self.modelVerticalLayout.addWidget(self.modelComboBox)

        # Add model combobox to options vertical layout
        self.optionsVerticalLayout.addLayout(self.modelVerticalLayout)

        # Create fuel type vertical layout
        self.fuelTypeVerticalLayout = QVBoxLayout()
        self.fuelTypeVerticalLayout.setSpacing(0)
        self.fuelTypeVerticalLayout.setObjectName(u"fuelTypeVerticalLayout")

        # Create fuel type label
        self.fuelTypeLabel = QLabel(self.optionsMainLayout)
        self.fuelTypeLabel.setObjectName(u"fuelTypeLabel")
        self.fuelTypeLabel.setFont(default_label_font)

        # Add fuel type label to fuel type vertical layout
        self.fuelTypeVerticalLayout.addWidget(self.fuelTypeLabel)

        # Create fuel type combobox
        self.fuelTypeComboBox = QComboBox(self.optionsMainLayout)
        self.fuelTypeComboBox.addItem("")
        self.fuelTypeComboBox.addItem("")
        self.fuelTypeComboBox.addItem("")
        self.fuelTypeComboBox.addItem("")
        self.fuelTypeComboBox.setObjectName(u"fuelTypeComboBox")
        self.fuelTypeComboBox.setFont(default_label_font)

        # Add fuel type combobox to fuel type vertical layout
        self.fuelTypeVerticalLayout.addWidget(self.fuelTypeComboBox)

        # Add fuel type vertical layout to options vertical layout
        self.optionsVerticalLayout.addLayout(self.fuelTypeVerticalLayout)

        # Create mileage vertical layout
        self.mileageVerticalLayout = QVBoxLayout()
        self.mileageVerticalLayout.setSpacing(0)
        self.mileageVerticalLayout.setObjectName(u"mileageVerticalLayout")
        self.mileageVerticalLayout.setContentsMargins(-1, -1, 0, -1)

        # Create mileage label
        self.mileageLabel = QLabel(self.optionsMainLayout)
        self.mileageLabel.setObjectName(u"mileageLabel")
        self.mileageLabel.setFont(default_label_font)

        # Add mileage label to mileage vertical layout
        self.mileageVerticalLayout.addWidget(self.mileageLabel)

        # Create mileage line edit
        self.mileageLineEdit = QLineEdit(self.optionsMainLayout)
        self.mileageLineEdit.setObjectName(u"mileageLineEdit")
        self.mileageLineEdit.setFont(default_label_font)

        # Create an integer validator to only allow numeric input
        mileage_validator = QIntValidator(0, 999999, self.mileageLineEdit)
        self.mileageLineEdit.setValidator(mileage_validator)

        # Add mileage line edit to mileage vertical layout
        self.mileageVerticalLayout.addWidget(self.mileageLineEdit)

        # Add mileage vertical layout to options vertical layout
        self.optionsVerticalLayout.addLayout(self.mileageVerticalLayout)

        # Create engine size vertical layout
        self.engineSizeVerticalLayout = QVBoxLayout()
        self.engineSizeVerticalLayout.setSpacing(0)
        self.engineSizeVerticalLayout.setObjectName(u"engineSizeVerticalLayout")

        # Create engine size label
        self.engineSizeLabel = QLabel(self.optionsMainLayout)
        self.engineSizeLabel.setObjectName(u"engineSizeLabel")
        self.engineSizeLabel.setFont(default_label_font)

        # Add engine size label to engine size vertical layout
        self.engineSizeVerticalLayout.addWidget(self.engineSizeLabel)

        # Create engine size line edit
        self.engineSizeLineEdit = QLineEdit(self.optionsMainLayout)
        self.engineSizeLineEdit.setObjectName(u"engineSizeLineEdit")
        self.engineSizeLineEdit.setFont(default_label_font)

        # Create QDoubleValidator for float values in the range [0.0, 10.0]
        engine_size_validator = CustomValidator()
        self.engineSizeLineEdit.setValidator(engine_size_validator)

        # Add engine size edit to engine size vertical layout
        self.engineSizeVerticalLayout.addWidget(self.engineSizeLineEdit)

        # Add engine size vertical layout to options vertical layout
        self.optionsVerticalLayout.addLayout(self.engineSizeVerticalLayout)

        # Create mpg main layout
        self.mpgMainLayout = QWidget(self)
        self.mpgMainLayout.setObjectName(u"verticalLayoutWidget_6")
        self.mpgMainLayout.setGeometry(QRect(30, 340, 81, 131))

        # Create mpg vertical layout
        self.mpgVerticalLayout = QVBoxLayout(self.mpgMainLayout)
        self.mpgVerticalLayout.setSpacing(0)
        self.mpgVerticalLayout.setObjectName(u"mpgVerticalLayout")
        self.mpgVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # Create mpg label
        self.mpgLabel = QLabel(self.mpgMainLayout)
        self.mpgLabel.setObjectName(u"mpgLabel")
        self.mpgLabel.setFont(default_label_font)
        self.mpgLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add mpg label to mpg vertical layout
        self.mpgVerticalLayout.addWidget(self.mpgLabel)

        # Create mpg dial
        self.mpgDial = QDial(self.mpgMainLayout)
        self.mpgDial.setObjectName(u"mpgDial")
        self.mpgDial.setMinimum(1)  # Set minimum value
        self.mpgDial.setMaximum(500)  # Set maximum value
        self.mpgDial.setValue(1)  # Set initial value

        # Connect mpg dial valueChanged signal to a custom slot
        self.mpgDial.valueChanged.connect(self.update_mpg_number_label)

        # Create mpg number label
        self.mpgNumberLabel = QLabel(self.mpgMainLayout)
        self.mpgNumberLabel.setObjectName(u"mpgNumberLabel")
        self.mpgNumberLabel.setFont(default_label_font)
        self.mpgNumberLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add mpg dial to the mpg vertical layout
        self.mpgVerticalLayout.addWidget(self.mpgDial)

        # Add mpg number label to the mpg vertical layout
        self.mpgVerticalLayout.addWidget(self.mpgNumberLabel)

        # Create tax main layout
        self.taxMainLayout = QWidget(self)
        self.taxMainLayout.setObjectName(u"verticalLayoutWidget_8")
        self.taxMainLayout.setGeometry(QRect(110, 340, 81, 131))

        # Create tax vertical layout
        self.taxVerticalLayout = QVBoxLayout(self.taxMainLayout)
        self.taxVerticalLayout.setSpacing(0)
        self.taxVerticalLayout.setObjectName(u"taxVerticalLayout")
        self.taxVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # Create tax label
        self.taxLabel = QLabel(self.taxMainLayout)
        self.taxLabel.setObjectName(u"taxLabel")
        self.taxLabel.setFont(default_label_font)
        self.taxLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add tax label to tax vertical layout
        self.taxVerticalLayout.addWidget(self.taxLabel)

        # Create tax dial
        self.taxDial = QDial(self.taxMainLayout)
        self.taxDial.setObjectName(u"taxDial")
        self.taxDial.setMinimum(1)  # Set minimum value
        self.taxDial.setMaximum(1000)  # Set maximum value
        self.taxDial.setValue(1)  # Set initial value

        # Add tax dial to tax vertical layout
        self.taxVerticalLayout.addWidget(self.taxDial)

        # Connect dial valueChanged signal to a custom slot
        self.taxDial.valueChanged.connect(self.update_tax_number_label)

        # Create tax number label
        self.taxNumberLabel = QLabel(self.taxMainLayout)
        self.taxNumberLabel.setObjectName(u"taxNumberLabel")
        self.taxNumberLabel.setFont(default_label_font)
        self.taxNumberLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add tax number label to tax vertical layout
        self.taxVerticalLayout.addWidget(self.taxNumberLabel)

        # Create year main layout
        self.yearMainLayout = QWidget(self)
        self.yearMainLayout.setObjectName(u"verticalLayoutWidget_7")
        self.yearMainLayout.setGeometry(QRect(30, 480, 431, 53))

        # Create year vertical layout
        self.yearVerticalLayout = QVBoxLayout(self.yearMainLayout)
        self.yearVerticalLayout.setObjectName(u"yearVerticalLayout")
        self.yearVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # Create year horizontal layout
        self.yearHorizontalLayout = QHBoxLayout()
        self.yearHorizontalLayout.setSpacing(10)
        self.yearHorizontalLayout.setObjectName(u"yearHorizontalLayout")

        # Create year label
        self.yearLabel = QLabel(self.yearMainLayout)
        self.yearLabel.setObjectName(u"yearLabel")
        self.yearLabel.setEnabled(True)
        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.yearLabel.sizePolicy().hasHeightForWidth())
        self.yearLabel.setSizePolicy(size_policy)
        self.yearLabel.setFont(default_label_font)
        self.yearLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading |
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter)

        # Add year label to year horizontal layout
        self.yearHorizontalLayout.addWidget(self.yearLabel)

        # Create year number label
        self.yearNumberLabel = QLabel(self.yearMainLayout)
        self.yearNumberLabel.setObjectName(u"yearNumberLabel")
        self.yearNumberLabel.setFont(default_label_font)
        self.yearNumberLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading |
            Qt.AlignmentFlag.AlignLeft |
            Qt.AlignmentFlag.AlignVCenter)

        # Add year number label to year horizontal layout
        self.yearHorizontalLayout.addWidget(self.yearNumberLabel)

        # Create year slider
        self.yearSlider = QSlider(self.yearMainLayout)
        self.yearSlider.setObjectName(u"yearSlider")
        self.yearSlider.setRange(2000, 2024)  # Set the range of values for the slider
        self.yearSlider.setValue(2000)  # Set initial value
        self.yearSlider.setFont(default_label_font)
        self.yearSlider.setOrientation(Qt.Orientation.Horizontal)

        # Connect year slider valueChanged signal to a custom slot
        self.yearSlider.valueChanged.connect(self.update_year_number_label)

        # Add year slider to year vertical layout
        self.yearVerticalLayout.addWidget(self.yearSlider)

        # Add year horizontal layout to year vertical layout
        self.yearVerticalLayout.addLayout(self.yearHorizontalLayout)

        # Create transmission main layout
        self.transmissionMainLayout = QWidget(self)
        self.transmissionMainLayout.setObjectName(u"horizontalLayoutWidget")
        self.transmissionMainLayout.setGeometry(QRect(30, 530, 431, 41))

        # Create transmission horizontal layout
        self.transmissionHorizontalLayout = QHBoxLayout(self.transmissionMainLayout)
        self.transmissionHorizontalLayout.setSpacing(0)
        self.transmissionHorizontalLayout.setObjectName(u"transmissionHorizontalLayout")
        self.transmissionHorizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Create transmission label
        self.transmissionLabel = QLabel(self.transmissionMainLayout)
        self.transmissionLabel.setObjectName(u"transmissionLabel")
        self.transmissionLabel.setFont(default_label_font)

        # Add transmission label to transmission horizontal layout
        self.transmissionHorizontalLayout.addWidget(self.transmissionLabel)

        # Create transmission horizontal layout 2
        self.transmissionHorizontalLayout_2 = QHBoxLayout()
        self.transmissionHorizontalLayout_2.setSpacing(10)
        self.transmissionHorizontalLayout_2.setObjectName(u"transmissionHorizontalLayout_2")

        # Create manual radio button
        self.manualRadioButton = QRadioButton(self.transmissionMainLayout)
        self.manualRadioButton.setObjectName(u"manualRadioButton")
        self.manualRadioButton.setFont(default_label_font)

        # Add manual radio button to transmission horizontal layout 2
        self.transmissionHorizontalLayout_2.addWidget(self.manualRadioButton)

        # Create auto radio button
        self.autoRadioButton = QRadioButton(self.transmissionMainLayout)
        self.autoRadioButton.setObjectName(u"autoRadioButton")
        self.autoRadioButton.setFont(default_label_font)

        # Add auto radio button to transmission horizontal layout 2
        self.transmissionHorizontalLayout_2.addWidget(self.autoRadioButton)

        # Create semi auto radio button
        self.semiAutoRadioButton = QRadioButton(self.transmissionMainLayout)
        self.semiAutoRadioButton.setObjectName(u"semiAutoRadioButton")
        self.semiAutoRadioButton.setFont(default_label_font)

        # Add semi auto radio button to transmission horizontal layout 2
        self.transmissionHorizontalLayout_2.addWidget(self.semiAutoRadioButton)

        # Create other radio button
        self.otherRadioButton = QRadioButton(self.transmissionMainLayout)
        self.otherRadioButton.setObjectName(u"otherRadioButton")
        self.otherRadioButton.setFont(default_label_font)

        # Add other radio button to transmission horizontal layout 2
        self.transmissionHorizontalLayout_2.addWidget(self.otherRadioButton)

        # Add transmission horizontal layout 2 to transmission horizontal layout
        self.transmissionHorizontalLayout.addLayout(self.transmissionHorizontalLayout_2)

        # Create switch variable label
        self.switchVariableLabel = QLabel(self)
        self.switchVariableLabel.setObjectName(u"switchVariableLabel")
        self.switchVariableLabel.setGeometry(QRect(200, 30, 251, 31))
        self.switchVariableLabel.setFont(default_label_font)
        self.switchVariableLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create last variable button
        self.lastVariableButton = QPushButton(self)
        self.lastVariableButton.setObjectName(u"lastVariableButton")
        self.lastVariableButton.setGeometry(QRect(460, 30, 41, 31))
        self.lastVariableButton.setFont(default_label_font)

        # Connect the button's clicked signal to a custom slot
        self.lastVariableButton.clicked.connect(self.on_last_variable_button_clicked)

        # Create next variable button
        self.nextVariableButton = QPushButton(self)
        self.nextVariableButton.setObjectName(u"nextVariableButton")
        self.nextVariableButton.setGeometry(QRect(500, 30, 41, 31))
        self.nextVariableButton.setFont(default_label_font)

        # Connect the button's clicked signal to a custom slot
        self.nextVariableButton.clicked.connect(self.on_next_variable_button_clicked)

        # Create current variable label
        self.currentVariableLabel = QLabel(self)
        self.currentVariableLabel.setObjectName(u"currentVariableLabel")
        self.currentVariableLabel.setGeometry(QRect(550, 30, 121, 31))
        self.currentVariableLabel.setFont(default_label_font)
        self.currentVariableLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create current variable result label
        self.currentVariableResultLabel = QLabel(self)
        self.currentVariableResultLabel.setObjectName(u"currentVariableResultLabel")
        self.currentVariableResultLabel.setGeometry(QRect(680, 30, 91, 31))
        self.currentVariableResultLabel.setFont(default_label_font)

        # Create car price graphics view
        self.carPriceGraphicsView = QWidget(self)
        self.carPriceGraphicsView.setObjectName(u"carPriceGraphicsView")
        self.carPriceGraphicsView.setObjectName(u"carPriceGraphicsView")
        self.carPriceGraphicsView.setGeometry(QRect(200, 60, 571, 361))

        self.scatterMainLayout = QVBoxLayout(self.carPriceGraphicsView)

        # Select 100 random rows from your DataFrame
        self.random_sample_df = self.df.sample(n=100, random_state=42)

        # Create a scatter plot for mileage vs. price
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

        # Initialize the index to 0
        self.current_variable_index = 0

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

        # Create predicted price main layout
        self.predictedPriceMainLayout = QWidget(self)
        self.predictedPriceMainLayout.setObjectName(u"horizontalLayoutWidget_3")
        self.predictedPriceMainLayout.setGeometry(QRect(520, 530, 221, 41))

        # Create predicted price horizontal layout
        self.predictedPriceHorizontalLayout = QHBoxLayout(self.predictedPriceMainLayout)
        self.predictedPriceHorizontalLayout.setObjectName(u"predictedPriceHorizontalLayout")
        self.predictedPriceHorizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Create predicted price label
        self.predictedPriceLabel = QLabel(self.predictedPriceMainLayout)
        self.predictedPriceLabel.setObjectName(u"predictedPriceLabel")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.predictedPriceLabel.setFont(font1)
        self.predictedPriceLabel.setAutoFillBackground(False)

        # Add predicted price label to predicted price horizontal layout
        self.predictedPriceHorizontalLayout.addWidget(self.predictedPriceLabel)

        # Create predicted price number label
        self.predictedPriceNumberLabel = QLabel(self.predictedPriceMainLayout)
        self.predictedPriceNumberLabel.setObjectName(u"predictedPriceNumberLabel")
        self.predictedPriceNumberLabel.setFont(font1)
        self.predictedPriceNumberLabel.setStyleSheet(u"color: rgb(132, 49, 165);")
        self.predictedPriceNumberLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add predicted price number label to predicted price horizontal layout
        self.predictedPriceHorizontalLayout.addWidget(self.predictedPriceNumberLabel)

        # Create mpg description label
        self.mpgDescription = QLabel(self)
        self.mpgDescription.setObjectName(u"mpgDescription")
        self.mpgDescription.setGeometry(QRect(200, 430, 261, 21))
        self.mpgDescription.setFont(default_description_font)

        # Create tax description label
        self.taxDescription = QLabel(self)
        self.taxDescription.setObjectName(u"taxDescription")
        self.taxDescription.setGeometry(QRect(200, 451, 261, 21))
        self.taxDescription.setFont(default_description_font)

        # Create the predict price button
        self.predictPriceButton = QPushButton(self)
        self.predictPriceButton.setObjectName(u"predictPriceButton")
        self.predictPriceButton.setGeometry(QRect(490, 480, 281, 41))
        self.predictPriceButton.setFont(default_label_font)
        self.predictPriceButton.setFlat(False)
        self.predictPriceButton.setDefault(False)

        # Connect the button's clicked signal to a custom slot
        self.predictPriceButton.clicked.connect(self.on_predict_price_button_clicked)

        # Update the user interface elements with translated text based on the current language.
        self.retranslate_ui(self)
        # Connect signals to slots based on the object names in the UI file.
        QMetaObject.connectSlotsByName(self)

    # This function is responsible for translating the UI elements to the desired language.
    # It sets the text for various labels, combo boxes, line edits, and buttons in the UI.
    def retranslate_ui(self, car_price_prediction_dialog):
        # Set window title
        car_price_prediction_dialog.setWindowTitle(QCoreApplication.translate("carPricePredictionDialog",
                                                                              u"Car Price Prediction", None))

        # Set text for brand labels and items in the brand combo box
        self.brandLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Brand:"))
        self.brandComboBox.setItemText(0, QCoreApplication.translate("carPricePredictionDialog", u"Audi", None))
        self.brandComboBox.setItemText(1, QCoreApplication.translate("carPricePredictionDialog", u"BMW", None))
        self.brandComboBox.setItemText(2, QCoreApplication.translate("carPricePredictionDialog", u"Ford", None))
        self.brandComboBox.setItemText(3, QCoreApplication.translate("carPricePredictionDialog", u"Toyota", None))

        # Set text for model labels and items in the model combo box
        self.modelLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Model:", None))
        self.modelComboBox.setItemText(0, QCoreApplication.translate("carPricePredictionDialog", u"1 Series", None))
        self.modelComboBox.setItemText(1, QCoreApplication.translate("carPricePredictionDialog", u"2 Series", None))
        self.modelComboBox.setItemText(2, QCoreApplication.translate("carPricePredictionDialog", u"3 Series", None))
        self.modelComboBox.setItemText(3, QCoreApplication.translate("carPricePredictionDialog", u"4 Series", None))
        self.modelComboBox.setItemText(4, QCoreApplication.translate("carPricePredictionDialog", u"5 Series", None))
        self.modelComboBox.setItemText(5, QCoreApplication.translate("carPricePredictionDialog", u"6 Series", None))
        self.modelComboBox.setItemText(6, QCoreApplication.translate("carPricePredictionDialog", u"7 Series", None))
        self.modelComboBox.setItemText(7, QCoreApplication.translate("carPricePredictionDialog", u"8 Series", None))
        self.modelComboBox.setItemText(8, QCoreApplication.translate("carPricePredictionDialog", u"A1", None))
        self.modelComboBox.setItemText(9, QCoreApplication.translate("carPricePredictionDialog", u"A2", None))
        self.modelComboBox.setItemText(10, QCoreApplication.translate("carPricePredictionDialog", u"A3", None))
        self.modelComboBox.setItemText(11, QCoreApplication.translate("carPricePredictionDialog", u"A4", None))
        self.modelComboBox.setItemText(12, QCoreApplication.translate("carPricePredictionDialog", u"A5", None))
        self.modelComboBox.setItemText(13, QCoreApplication.translate("carPricePredictionDialog", u"A6", None))
        self.modelComboBox.setItemText(14, QCoreApplication.translate("carPricePredictionDialog", u"A7", None))
        self.modelComboBox.setItemText(15, QCoreApplication.translate("carPricePredictionDialog", u"A8", None))
        self.modelComboBox.setItemText(16, QCoreApplication.translate("carPricePredictionDialog", u"Auris", None))
        self.modelComboBox.setItemText(17, QCoreApplication.translate("carPricePredictionDialog", u"Avensis", None))
        self.modelComboBox.setItemText(18, QCoreApplication.translate("carPricePredictionDialog", u"Aygo", None))
        self.modelComboBox.setItemText(19, QCoreApplication.translate("carPricePredictionDialog", u"B-MAX", None))
        self.modelComboBox.setItemText(20, QCoreApplication.translate("carPricePredictionDialog", u"C-HR", None))
        self.modelComboBox.setItemText(21, QCoreApplication.translate("carPricePredictionDialog", u"C-MAX", None))
        self.modelComboBox.setItemText(22, QCoreApplication.translate("carPricePredictionDialog", u"Camry", None))
        self.modelComboBox.setItemText(23, QCoreApplication.translate("carPricePredictionDialog", u"Corolla", None))
        self.modelComboBox.setItemText(24, QCoreApplication.translate("carPricePredictionDialog", u"EcoSport", None))
        self.modelComboBox.setItemText(25, QCoreApplication.translate("carPricePredictionDialog", u"Edge", None))
        self.modelComboBox.setItemText(26, QCoreApplication.translate("carPricePredictionDialog", u"Escort", None))
        self.modelComboBox.setItemText(27, QCoreApplication.translate("carPricePredictionDialog", u"Fiesta", None))
        self.modelComboBox.setItemText(28, QCoreApplication.translate("carPricePredictionDialog", u"Focus", None))
        self.modelComboBox.setItemText(29, QCoreApplication.translate("carPricePredictionDialog", u"Fusion", None))
        self.modelComboBox.setItemText(30, QCoreApplication.translate("carPricePredictionDialog", u"GT86", None))
        self.modelComboBox.setItemText(31, QCoreApplication.translate("carPricePredictionDialog", u"Galaxy", None))
        self.modelComboBox.setItemText(32, QCoreApplication.translate("carPricePredictionDialog", u"Grand C-MAX", None))
        self.modelComboBox.setItemText(33,
                                       QCoreApplication.translate("carPricePredictionDialog", u"Grand Tourneo Connect",
                                                                  None))
        self.modelComboBox.setItemText(34, QCoreApplication.translate("carPricePredictionDialog", u"Hilux", None))
        self.modelComboBox.setItemText(35, QCoreApplication.translate("carPricePredictionDialog", u"IQ", None))
        self.modelComboBox.setItemText(36, QCoreApplication.translate("carPricePredictionDialog", u"KA", None))
        self.modelComboBox.setItemText(37, QCoreApplication.translate("carPricePredictionDialog", u"Ka+", None))
        self.modelComboBox.setItemText(38, QCoreApplication.translate("carPricePredictionDialog", u"Kuga", None))
        self.modelComboBox.setItemText(39,
                                       QCoreApplication.translate("carPricePredictionDialog", u"Land Cruiser", None))
        self.modelComboBox.setItemText(40, QCoreApplication.translate("carPricePredictionDialog", u"M2", None))
        self.modelComboBox.setItemText(41, QCoreApplication.translate("carPricePredictionDialog", u"M3", None))
        self.modelComboBox.setItemText(42, QCoreApplication.translate("carPricePredictionDialog", u"M4", None))
        self.modelComboBox.setItemText(43, QCoreApplication.translate("carPricePredictionDialog", u"M5", None))
        self.modelComboBox.setItemText(44, QCoreApplication.translate("carPricePredictionDialog", u"M6", None))
        self.modelComboBox.setItemText(45, QCoreApplication.translate("carPricePredictionDialog", u"Mondeo", None))
        self.modelComboBox.setItemText(46, QCoreApplication.translate("carPricePredictionDialog", u"Mustang", None))
        self.modelComboBox.setItemText(47,
                                       QCoreApplication.translate("carPricePredictionDialog", u"PROACE VERSO", None))
        self.modelComboBox.setItemText(48, QCoreApplication.translate("carPricePredictionDialog", u"Prius", None))
        self.modelComboBox.setItemText(49, QCoreApplication.translate("carPricePredictionDialog", u"Puma", None))
        self.modelComboBox.setItemText(50, QCoreApplication.translate("carPricePredictionDialog", u"Q2", None))
        self.modelComboBox.setItemText(51, QCoreApplication.translate("carPricePredictionDialog", u"Q3", None))
        self.modelComboBox.setItemText(52, QCoreApplication.translate("carPricePredictionDialog", u"Q5", None))
        self.modelComboBox.setItemText(53, QCoreApplication.translate("carPricePredictionDialog", u"Q7", None))
        self.modelComboBox.setItemText(54, QCoreApplication.translate("carPricePredictionDialog", u"Q8", None))
        self.modelComboBox.setItemText(55, QCoreApplication.translate("carPricePredictionDialog", u"R8", None))
        self.modelComboBox.setItemText(56, QCoreApplication.translate("carPricePredictionDialog", u"RAV4", None))
        self.modelComboBox.setItemText(57, QCoreApplication.translate("carPricePredictionDialog", u"RS3", None))
        self.modelComboBox.setItemText(58, QCoreApplication.translate("carPricePredictionDialog", u"RS4", None))
        self.modelComboBox.setItemText(59, QCoreApplication.translate("carPricePredictionDialog", u"RS5", None))
        self.modelComboBox.setItemText(60, QCoreApplication.translate("carPricePredictionDialog", u"RS6", None))
        self.modelComboBox.setItemText(61, QCoreApplication.translate("carPricePredictionDialog", u"RS7", None))
        self.modelComboBox.setItemText(62, QCoreApplication.translate("carPricePredictionDialog", u"Ranger", None))
        self.modelComboBox.setItemText(63, QCoreApplication.translate("carPricePredictionDialog", u"S-MAX", None))
        self.modelComboBox.setItemText(64, QCoreApplication.translate("carPricePredictionDialog", u"S3", None))
        self.modelComboBox.setItemText(65, QCoreApplication.translate("carPricePredictionDialog", u"S4", None))
        self.modelComboBox.setItemText(66, QCoreApplication.translate("carPricePredictionDialog", u"S5", None))
        self.modelComboBox.setItemText(67, QCoreApplication.translate("carPricePredictionDialog", u"S8", None))
        self.modelComboBox.setItemText(68, QCoreApplication.translate("carPricePredictionDialog", u"SQ5", None))
        self.modelComboBox.setItemText(69, QCoreApplication.translate("carPricePredictionDialog", u"SQ7", None))
        self.modelComboBox.setItemText(70, QCoreApplication.translate("carPricePredictionDialog", u"Streetka", None))
        self.modelComboBox.setItemText(71, QCoreApplication.translate("carPricePredictionDialog", u"Supra", None))
        self.modelComboBox.setItemText(72, QCoreApplication.translate("carPricePredictionDialog", u"TT", None))
        self.modelComboBox.setItemText(73,
                                       QCoreApplication.translate("carPricePredictionDialog", u"Tourneo Connect", None))
        self.modelComboBox.setItemText(74,
                                       QCoreApplication.translate("carPricePredictionDialog", u"Tourneo Custom", None))
        self.modelComboBox.setItemText(75,
                                       QCoreApplication.translate("carPricePredictionDialog", u"Transit Tourneo", None))
        self.modelComboBox.setItemText(76,
                                       QCoreApplication.translate("carPricePredictionDialog", u"Urban Cruiser", None))
        self.modelComboBox.setItemText(77, QCoreApplication.translate("carPricePredictionDialog", u"Verso", None))
        self.modelComboBox.setItemText(78, QCoreApplication.translate("carPricePredictionDialog", u"Verso-S", None))
        self.modelComboBox.setItemText(79, QCoreApplication.translate("carPricePredictionDialog", u"X1", None))
        self.modelComboBox.setItemText(80, QCoreApplication.translate("carPricePredictionDialog", u"X2", None))
        self.modelComboBox.setItemText(81, QCoreApplication.translate("carPricePredictionDialog", u"X3", None))
        self.modelComboBox.setItemText(82, QCoreApplication.translate("carPricePredictionDialog", u"X4", None))
        self.modelComboBox.setItemText(83, QCoreApplication.translate("carPricePredictionDialog", u"X5", None))
        self.modelComboBox.setItemText(84, QCoreApplication.translate("carPricePredictionDialog", u"X6", None))
        self.modelComboBox.setItemText(85, QCoreApplication.translate("carPricePredictionDialog", u"X7", None))
        self.modelComboBox.setItemText(86, QCoreApplication.translate("carPricePredictionDialog", u"Yaris", None))
        self.modelComboBox.setItemText(87, QCoreApplication.translate("carPricePredictionDialog", u"Z3", None))
        self.modelComboBox.setItemText(88, QCoreApplication.translate("carPricePredictionDialog", u"Z4", None))
        self.modelComboBox.setItemText(89, QCoreApplication.translate("carPricePredictionDialog", u"i3", None))
        self.modelComboBox.setItemText(90, QCoreApplication.translate("carPricePredictionDialog", u"i8", None))

        # Set text for fuel type labels and items in the fuel type combo box
        self.fuelTypeLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Fuel type:", None))
        self.fuelTypeComboBox.setItemText(0, QCoreApplication.translate("carPricePredictionDialog", u"Diesel", None))
        self.fuelTypeComboBox.setItemText(1, QCoreApplication.translate("carPricePredictionDialog", u"Petrol", None))
        self.fuelTypeComboBox.setItemText(2, QCoreApplication.translate("carPricePredictionDialog", u"Hybrid", None))
        self.fuelTypeComboBox.setItemText(3, QCoreApplication.translate("carPricePredictionDialog", u"Other", None))

        # Set text for mileage type labels and placeholder in the line edit
        self.mileageLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Mileage:", None))
        self.mileageLineEdit.setPlaceholderText(
            QCoreApplication.translate("carPricePredictionDialog", u"(0-1000000)", None))

        # Set text for mileage type labels and placeholder in the line edit
        self.engineSizeLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Engine Size", None))
        self.engineSizeLineEdit.setPlaceholderText(
            QCoreApplication.translate("carPricePredictionDialog", u"(0-10)", None))

        # Set text for transmission label and radio buttons related to it
        self.transmissionLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Transmission:", None))
        self.manualRadioButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Manual", None))
        self.autoRadioButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Auto", None))
        self.semiAutoRadioButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Semi-Auto", None))
        self.otherRadioButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Other", None))

        # Set text for switch variable label
        self.switchVariableLabel.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"Switch variable you want to analyze:", None))

        # Set text for last variable button and next variable button
        self.lastVariableButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Last", None))
        self.nextVariableButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Next", None))

        # Set text for current variable label and current variable result label
        self.currentVariableLabel.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"Current variable:", None))
        self.currentVariableResultLabel.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"year", None))

        # Set text for predict price button
        self.predictPriceButton.setText(QCoreApplication.translate("carPricePredictionDialog", u"Predict price", None))

        # Set text for mpg label and the number
        self.mpgLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"MPG", None))
        self.mpgNumberLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"1", None))

        # Set text for year label and the number
        self.yearLabel.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"Year of production (2000 - 2024):", None))
        self.yearNumberLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"2000", None))

        # Set text for tax label and the number
        self.taxLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Tax", None))
        self.taxNumberLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"1", None))

        # Set text for predicted price label and the number
        self.predictedPriceLabel.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"Predicted price:", None))
        self.predictedPriceNumberLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"None", None))

        # Set text for mpg and tax description
        self.mpgDescription.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"MPG -miles per gallon, fuel use effciency ", None))
        self.taxDescription.setText(
            QCoreApplication.translate("carPricePredictionDialog", u"Tax - annual fee for vehicle ownership", None))

        # Set text for top model label and the result
        self.topModelLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Top Model", None))
        self.topModelResultLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"None", None))

        # Set text for avg mileage label and the result
        self.avgMileageLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Avg Mileage", None))
        self.avgMileageResultLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"0", None))

        # Set text for avg mpg label and the result
        self.avgMPGLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"Avg MPG", None))
        self.avgMPGResultLabel.setText(QCoreApplication.translate("carPricePredictionDialog", u"0", None))

    # These three functions are used to update the text of labels displaying numeric values in the UI.
    # They are called when the corresponding values are changed elsewhere in the program.
    def update_mpg_number_label(self, value):
        self.mpgNumberLabel.setText(str(value))

    def update_tax_number_label(self, value):
        self.taxNumberLabel.setText(str(value))

    def update_year_number_label(self, value):
        self.yearNumberLabel.setText(str(value))

    def update_top_model_result_label(self):
        # Get the top 1 most popular model
        most_popular_model = self.df['model'].value_counts().idxmax()
        self.topModelResultLabel.setText(str(most_popular_model))

    def update_average_mileage_result_label(self):
        # Calculate average mileage
        average_mileage = self.df['mileage'].mean()
        self.avgMileageResultLabel.setText(str(int(average_mileage)))

    def update_average_mpg_result_label(self):
        # Calculate average MPG
        average_mpg = self.df['mpg'].mean()
        self.avgMPGResultLabel.setText(str(int(average_mpg)))

    def update_stats(self):
        self.update_top_model_result_label()
        self.update_average_mileage_result_label()
        self.update_average_mpg_result_label()

    # This function is called when the "Predict price" button is clicked.
    # It gathers values from various UI elements (brand, model, fuel type, mileage, transmission, dials, sliders),
    # and prints these values for demonstration purposes.
    def on_predict_price_button_clicked(self):
        # Get values from various UI elements
        brand_value = self.brandComboBox.currentText()
        model_value = self.modelComboBox.currentText()
        fuel_type_value = self.fuelTypeComboBox.currentText()
        mileage_value = self.mileageLineEdit.text()
        engine_size_value = self.engineSizeLineEdit.text()

        # Handle case when mileage is not provided
        if mileage_value == '':
            mileage_value = 0

        # Handle case when engineSize is not provided
        if engine_size_value == '':
            engine_size_value = 1

        # Get the selected transmission type
        if self.manualRadioButton.isChecked():
            transmission_value = "Manual"
        elif self.autoRadioButton.isChecked():
            transmission_value = "Automatic"
        elif self.semiAutoRadioButton.isChecked():
            transmission_value = "Semi-Auto"
        else:
            transmission_value = "Other"

        # Get values from dials and sliders
        mpg_value = self.mpgDial.value()
        tax_value = self.taxDial.value()
        year_value = self.yearSlider.value()

        # Print gathered values
        print("Brand:", brand_value)
        print("Model:", model_value)
        print("Fuel Type:", fuel_type_value)
        print("Mileage:", mileage_value)
        print("Engine Size:", engine_size_value)
        print("Transmission:", transmission_value)
        print("MPG Dial Value:", mpg_value)
        print("Tax Dial Value:", tax_value)
        print("Year Of Production Value:", year_value)

        # Encode the string values using the loaded encoding models
        encoded_brand_value = self.brand_label_encoder.transform([brand_value])[0]
        encoded_model_value = self.model_label_encoder.transform([model_value])[0]
        encoded_transmission_value = self.transmission_label_encoder.transform([transmission_value])[0]
        encoded_fuel_type_value = self.fuelType_label_encoder.transform([fuel_type_value])[0]

        # Transform the values using the loaded scaler models
        transformed_brand_value = self.brand_scaler_model.transform([[encoded_brand_value]])
        transformed_model_value = self.loaded_model_scaler_model.transform([[encoded_model_value]])
        transformed_year_value = self.year_scaler_model.transform([[year_value]])
        transformed_transmission_value = self.transmission_scaler_model.transform([[encoded_transmission_value]])
        transformed_mileage_value = self.mileage_scaler_model.transform([[mileage_value]])
        transformed_fuel_type_value = self.fuelType_scaler_model.transform([[encoded_fuel_type_value]])
        transformed_tax_value_value = self.tax_scaler_model.transform([[tax_value]])
        transformed_mpg_value = self.mpg_scaler_model.transform([[mpg_value]])
        transformed_engine_size_value = self.engineSize_scaler_model.transform([[engine_size_value]])

        # Create a list of transformed values
        scaled_new_value = ([[
            transformed_brand_value[0][0],
            transformed_model_value[0][0],
            transformed_year_value[0][0],
            transformed_transmission_value[0][0],
            transformed_mileage_value[0][0],
            transformed_fuel_type_value[0][0],
            transformed_tax_value_value[0][0],
            transformed_mpg_value[0][0],
            transformed_engine_size_value[0][0]
        ]])
        # Get a prediction from a model
        prediction = self.random_forest_model.predict(scaled_new_value)
        # Set the predicted price on the predicted price number label
        self.predictedPriceNumberLabel.setText(str(int(prediction[0])))
        self.predicted_price = str(int(prediction[0]))
        self.update_stats()
        self.update_plot()

    def on_last_variable_button_clicked(self):
        self.current_variable_index -= 1
        if self.current_variable_index < 0:
            self.current_variable_index = len(self.numeric_columns) - 1
        self.update_plot()

    def on_next_variable_button_clicked(self):
        self.current_variable_index += 1
        if self.current_variable_index >= len(self.numeric_columns):
            self.current_variable_index = 0
        self.update_plot()

    def update_plot(self):
        selected_variable = self.numeric_columns[self.current_variable_index]
        self.currentVariableResultLabel.setText(selected_variable.capitalize())

        # Update the scatter plot with the selected variable
        self.scatter_plot.clear()  # Clear the existing plot
        self.scatter_plot = sns.scatterplot(
            data=self.random_sample_df,
            y="price",
            x=selected_variable,
            ax=self.scatter_plot
        )

        # Get values from various UI elements
        mileage_value = self.mileageLineEdit.text()
        engine_size_value = self.engineSizeLineEdit.text()

        # Handle case when mileage is not provided
        if mileage_value == '':
            mileage_value = 0

        # Handle case when engineSize is not provided
        if engine_size_value == '':
            engine_size_value = 1

        # Get values from dials and sliders
        mpg_value = self.mpgDial.value()
        tax_value = self.taxDial.value()
        year_value = self.yearSlider.value()

        # Highlighted red point

        # The x-coordinate of the red point
        if selected_variable == "mileage":
            red_point_x = mileage_value
        elif selected_variable == "engineSize":
            red_point_x = engine_size_value
        elif selected_variable == "mpg":
            red_point_x = mpg_value
        elif selected_variable == "tax":
            red_point_x = tax_value
        else:
            red_point_x = year_value

        # The y-coordinate of the red point
        red_point_y = self.predicted_price

        if red_point_y is not None:
            self.scatter_plot.scatter(
                red_point_x,
                int(red_point_y),
                color='red',
                marker='x',
                s=100,
                label='Highlighted Point')

        self.scatter_plot.set_title(f"Scatter Plot: Price vs. {selected_variable.capitalize()}")
        # Customize xlabel and ylabel appearance
        self.scatter_plot.set_xlabel(selected_variable.capitalize(), fontsize=12, labelpad=5)
        self.scatter_plot.set_ylabel("Price", fontsize=12, labelpad=5)

        # Redraw the canvas
        self.scatter_canvas.draw()

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


# The following block initializes the application, creates a dialog, sets up the UI,
# and finally, shows the dialog.
def main():
    df = pd.read_csv('csv/cars.csv')
    app = QApplication(sys.argv)
    ui = UICarPricePredictionDialog(df)
    ui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
