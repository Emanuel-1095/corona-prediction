# =========================== Definición ====================== #

class Nanoparticles:

    models_filenames=['liposome_models', 'liposome_models_opt-np_type', 'liposome_models-np_type', 'modelos_guardados']
    dictionary_output_predictions= 
    {
        datos_np_unq_externo: 'datos_np_unq_externo-prediction_',
        datos_np_unq_: '',
        
    }
    
    def __init__ (self, csv_filename, selected_attributes=None, categorical_attributes=None, protein_tagets=None, ):
        self.csv_filename = csv_filename
        self.selected_attributes = selected_attributes
        self.categorical_attributes = categorical_attributes
        self.protein_tagets = protein_tagets
        
        self.
    

# =========================== Definición de funciones ====================== #

# Métricas de evaluación utilizadas en el paper original

# Función del R2
def paper_r2(y_true, y_pred):
    """Paper's metric: Pearson correlation"""
    corr = np.corrcoef(y_true, y_pred)[0, 1]
    return corr 

#Función del RMSE
def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))


# =========================== Selección de todos los atributos ========================= #

# =========================== 21 atributos seleccionados =========================== #

selected_21_attributes = [
    'np_without_modification', 'surface_modification', 'size_tem', 'zeta_potential', 
    'incubation_protein_source', 'incubation_plasma_concentration', 'incubation_np_concentration',
    'centrifugation_speed', 'centrifugation_time', 'centrifugation_temperature', 'np_type',
    'np_shape', 'dispersion_medium', 'dispersion_medium_ph', 'size_dls', 'pdi', 'incubation_culture',
    'incubation_time', 'incubation_temperature', 'centrifugation_repetitions', 'modification_type'
]


categorical_21_attributes = [
    'np_without_modification', 'surface_modification', 'incubation_protein_source',
    'np_type', 'np_shape', 'dispersion_medium', 'incubation_culture', 'modification_type'
]

# =========================== 10 atributos seleccionados =========================== #

selected_10_attributes = [
    'np_without_modification', 'surface_modification', 
    'incubation_protein_source', 'size_tem', 'zeta_potential', 'incubation_plasma_concentration', 
    'incubation_np_concentration','centrifugation_speed', 
    'centrifugation_time', 'centrifugation_temperature'    
]

categorical_10_attributes = [
    'np_without_modification', 'surface_modification', 'incubation_protein_source',
]

# =========================== 17 atributos seleccionados (Jair) =========================== #

selected_17_attributes = [
    'np_without_modification', 'surface_modification', 'zeta_potential', 
    'incubation_protein_source', 'incubation_plasma_concentration', 'incubation_np_concentration',
    'np_type', 'np_shape', 'dispersion_medium', 'dispersion_medium_ph', 'size_dls', 'pdi', 
    'incubation_culture', 'incubation_time', 'incubation_temperature', 'modification_type'
]

categorical_17_attributes = [
    'np_without_modification', 'surface_modification', 'incubation_protein_source',
    'np_type', 'np_shape', 'dispersion_medium', 'incubation_culture', 'modification_type'
]

# =========================== 16 atributos seleccionados (sin np_type para el entrenamiento) =========================== #

selected_16_attributes = [
    'np_without_modification', 'surface_modification', 'zeta_potential', 
    'incubation_protein_source', 'incubation_plasma_concentration', 'incubation_np_concentration', 
    'np_shape', 'dispersion_medium', 'dispersion_medium_ph', 'size_dls', 'pdi', 
    'incubation_culture', 'incubation_time', 'incubation_temperature', 'modification_type'
]

categorical_16_attributes = [
    'np_without_modification', 'surface_modification', 'incubation_protein_source',
    'np_shape', 'dispersion_medium', 'incubation_culture', 'modification_type'
]

# =========================== 178 Proteinas =========================== #

protein_targets = [
    "P01871", "P01024", "P02647", "P02649", "P02768", "P04004", "P01834", 
    "P10909", "P02652", "P00734", "P01009", "P01042", "P01857", "P01859", 
    "P01023", "P01619", "P04196", "P02656", "P04114", "P02787", "P02766", 
    "P06396", "P06727", "P0C0L5", "P02671", "P08603", "P02765", "Q14624", 
    "P0DOY2", "P01008", "P68871", "P01764", "P04003", "P0C0L4", "P01876", 
    "P02749", "P02675", "P01860", "P01011", "P00747", "P02774", "P00751", 
    "P19823", "P08697", "P19827", "P69905", "P02760", "P02748", "P02679", 
    "P02790", "B9A064", "P07996", "P05155", "P01766", "P12259", "P00738",
    "P02751", "P02654", "P04406", "P00739", "P02655", "P00736", "P07225", 
    "P05154", "P09871", "P60709", "P03952", "P02747", "P05546", "P02746",
    "P27169", "P01019", "P35542", "P04217", "Q14520", "P02743", "P02763", 
    "P49908", "O43866", "P18428", "P55056", "P04264", "P00748", "P01591", 
    "P01861", "Q92954", "P02776", "P0DJI8", "P01031", "P05156", "P13671", 
    "Q03591", "P06312", "P00740", "P01615", "P00742", "P04070", "O14791", 
    "P05090", "P02745", "P00488", "Q13103", "P01877", "P01700", "P10643", 
    "Q9UK55", "P03951", "Q06033", "Q96IY4", "P13645", "P04433", "P07358",
    "P27918", "P05452", "P20851", "P07357", "P07360", "P01599", "O95445", 
    "Q9BXR6", "P02775", "P02741", "P35579", "P15169", "Q13790", "P35858", 
    "P49747", "P36955", "P19652", "P07737", "P22891", "P35908", "P80748", 
    "P08514", "P01593", "Q04756", "P06733", "P23528", "P63104", "P18065", 
    "P08519", "Q86UX7", "P02753", "Q5TB80", "P22352", "P00746", "P35443", 
    "P62937", "P10720", "P48740", "P25311", "P43652", "P35527", "Q9Y490", 
    "P05106", "P17936", "P18206", "P02788", "P06702", "P01701", "Q6Q788", 
    "Q96PD5", "Q9UGM5", "O00391", "P11142", "P14618", "P23142", "P68366",
    "P12814", "P61224", "Q13201", "P67936", "P0DOY3", "P08709", "P01034", 
    "P81605", "P02533", "P11226"]

important_protein_targets = ["P02768", "P01024", "P0C0L5", "P0C0L4", "P0D0X6", "P02741", "P11226"]