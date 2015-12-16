from django.db import models

from wagtail.wagtailcore.models import Page


class HomePage(Page):
    pass


class RawDataMap(models.Model):
	import_id = models.CharField(max_length=100)
	identifier = models.CharField(max_length=200)

class DataPoint(models.Model):
	data_set = models.CharField(max_length=200)
	column_value = models.CharField(max_length=200)
	point_value = models.CharField(max_length=500)
	column_number = models.IntegerField()


class AirQualityDataPoint(models.Model):
	State_Code = models.CharField(max_length=1000, blank=True)
	County_Code = models.CharField(max_length=1000, blank=True)
	Site_Num = models.CharField(max_length=1000, blank=True)
	Parameter_Code = models.CharField(max_length=1000, blank=True)
	POC = models.CharField(max_length=1000, blank=True)
	Latitude = models.CharField(max_length=1000, blank=True)
	Longitude = models.CharField(max_length=1000, blank=True)
	Datum = models.CharField(max_length=1000, blank=True)
	Parameter_Name = models.CharField(max_length=1000, blank=True)
	Sample_Duration = models.CharField(max_length=1000, blank=True)
	Pollutant_Standard = models.CharField(max_length=1000, blank=True)
	Metric_Used = models.CharField(max_length=1000, blank=True)
	Method_Name = models.CharField(max_length=1000, blank=True)
	Year = models.CharField(max_length=1000, blank=True)
	Units_of_Measure = models.CharField(max_length=1000, blank=True)
	Event_Type = models.CharField(max_length=1000, blank=True)
	Observation_Count = models.CharField(max_length=1000, blank=True)
	Observation_Percent = models.CharField(max_length=1000, blank=True)
	Completeness_Indicator = models.CharField(max_length=1000, blank=True)
	Valid_Day_Count = models.CharField(max_length=1000, blank=True)
	Required_Day_Count = models.CharField(max_length=1000, blank=True)
	Exceptional_Data_Count = models.CharField(max_length=1000, blank=True)
	Null_Data_Count = models.CharField(max_length=1000, blank=True)
	Primary_Exceedance_Count = models.CharField(max_length=1000, blank=True)
	Secondary_Exceedance_Count = models.CharField(max_length=1000, blank=True)
	Certification_Indicator = models.CharField(max_length=1000, blank=True)
	Num_Obs_Below_MDL = models.CharField(max_length=1000, blank=True)
	Arithmetic_Mean = models.CharField(max_length=1000, blank=True)
	Arithmetic_Standard_Dev = models.CharField(max_length=1000, blank=True)
	onest_Max_Value = models.CharField(max_length=1000, blank=True)
	onest_Max_DateTime = models.CharField(max_length=1000, blank=True)
	twod_Max_Value = models.CharField(max_length=1000, blank=True)
	twond_Max_DateTime = models.CharField(max_length=1000, blank=True)
	threerd_Max_Value = models.CharField(max_length=1000, blank=True)
	threerd_Max_DateTime = models.CharField(max_length=1000, blank=True)
	fourthth_Max_Value = models.CharField(max_length=1000, blank=True)
	fourthth_Max_DateTime = models.CharField(max_length=1000, blank=True)
	onest_Max_Non_Overlapping_Value = models.CharField(max_length=1000, blank=True)
	onest_NO_Max_DateTime = models.CharField(max_length=1000, blank=True)
	twond_Max_Non_Overlapping_Value = models.CharField(max_length=1000, blank=True)
	twond_NO_Max_DateTime = models.CharField(max_length=1000, blank=True)
	ninenineth_Percentile = models.CharField(max_length=1000, blank=True)
	nineeightth_Percentile = models.CharField(max_length=1000, blank=True)
	ninefiveth_Percentile = models.CharField(max_length=1000, blank=True)
	ninezeroth_Percentile = models.CharField(max_length=1000, blank=True)
	sevenfiveth_Percentile = models.CharField(max_length=1000, blank=True)
	fivezeroth_Percentile = models.CharField(max_length=1000, blank=True)
	onezeroth_Percentile = models.CharField(max_length=1000, blank=True)
	Local_Site_Name = models.CharField(max_length=1000, blank=True)
	Address = models.CharField(max_length=1000, blank=True)
	State_Name = models.CharField(max_length=1000, blank=True)
	County_Name = models.CharField(max_length=1000, blank=True)
	City_Name = models.CharField(max_length=1000, blank=True)
	CBSA_Name = models.CharField(max_length=1000, blank=True)
	Date_of_Last_Change = models.CharField(max_length=1000, blank=True)

	def __unicode__(self):
		return self.Arithmetic_Mean + " " + self.Units_of_Measure + " " + self.Parameter_Name


class ToxicDataPoint(models.Model):
	FORM_TYPE = models.CharField(max_length=1000, blank=True)
	REPORTING_YEAR = models.CharField(max_length=1000, blank=True)
	TRADE_SECRET_INDICATOR = models.CharField(max_length=1000, blank=True)
	SANITIZED_INDICATOR = models.CharField(max_length=1000, blank=True)
	TITLE_OF_CERTIFYING_OFFICIAL = models.CharField(max_length=1000, blank=True)
	NAME_OF_CERTIFYING_OFFICIAL = models.CharField(max_length=1000, blank=True)
	CERTIFYING_OFFICIALS_SIGNATURE_INDICATOR = models.CharField(max_length=1000, blank=True)
	DATE_SIGNED = models.CharField(max_length=1000, blank=True)
	TRIFID = models.CharField(max_length=1000, blank=True)
	FACILITY_NAME = models.CharField(max_length=1000, blank=True)
	FACILITY_STREET = models.CharField(max_length=1000, blank=True)
	FACILITY_CITY = models.CharField(max_length=1000, blank=True)
	FACILITY_COUNTY = models.CharField(max_length=1000, blank=True)
	FACILITY_STATE = models.CharField(max_length=1000, blank=True)
	FACILITY_ZIP_CODE = models.CharField(max_length=1000, blank=True)
	FACILITY_BIA_CODE = models.CharField(max_length=1000, blank=True)
	FACILITY_BIA_NAME = models.CharField(max_length=1000, blank=True)
	MAILING_NAME = models.CharField(max_length=1000, blank=True)
	MAILING_STREET = models.CharField(max_length=1000, blank=True)
	MAILING_CITY = models.CharField(max_length=1000, blank=True)
	MAILING_STATE = models.CharField(max_length=1000, blank=True)
	MAILING_PROVINCE = models.CharField(max_length=1000, blank=True)
	MAILING_ZIP_CODE = models.CharField(max_length=1000, blank=True)
	ENTIRE_FACILITY_IND = models.CharField(max_length=1000, blank=True)
	PARTIAL_FACILITY_IND = models.CharField(max_length=1000, blank=True)
	FEDERAL_FACILITY_IND = models.CharField(max_length=1000, blank=True)
	GOCO_FACILITY_IND = models.CharField(max_length=1000, blank=True)
	PUBLIC_CONTACT_NAME = models.CharField(max_length=1000, blank=True)
	PUBLIC_CONTACT_PHONE = models.CharField(max_length=1000, blank=True)
	PRIMARY_SIC_CODE = models.CharField(max_length=1000, blank=True)
	SIC_CODE_2 = models.CharField(max_length=1000, blank=True)
	SIC_CODE_3 = models.CharField(max_length=1000, blank=True)
	SIC_CODE_4 = models.CharField(max_length=1000, blank=True)
	SIC_CODE_5 = models.CharField(max_length=1000, blank=True)
	SIC_CODE_6 = models.CharField(max_length=1000, blank=True)
	NAICS_ORIGIN = models.CharField(max_length=1000, blank=True)
	PRIMARY_NAICS_CODE = models.CharField(max_length=1000, blank=True)
	NAICS_CODE_2 = models.CharField(max_length=1000, blank=True)
	NAICS_CODE_3 = models.CharField(max_length=1000, blank=True)
	NAICS_CODE_4 = models.CharField(max_length=1000, blank=True)
	NAICS_CODE_5 = models.CharField(max_length=1000, blank=True)
	NAICS_CODE_6 = models.CharField(max_length=1000, blank=True)
	LATITUDE = models.CharField(max_length=1000, blank=True)
	LONGITUDE = models.CharField(max_length=1000, blank=True)
	DB_NR_A = models.CharField(max_length=1000, blank=True)
	DB_NR_B = models.CharField(max_length=1000, blank=True)
	RCRA_NR_A = models.CharField(max_length=1000, blank=True)
	RCRA_NR_B = models.CharField(max_length=1000, blank=True)
	NPDES_NR_A = models.CharField(max_length=1000, blank=True)
	NPDES_NR_B = models.CharField(max_length=1000, blank=True)
	UIC_NR_A = models.CharField(max_length=1000, blank=True)
	UIC_NR_B = models.CharField(max_length=1000, blank=True)
	PARENT_COMPANY_NAME = models.CharField(max_length=1000, blank=True)
	PARENT_COMPANY_DB_NR = models.CharField(max_length=1000, blank=True)
	DOCUMENT_CONTROL_NUMBER = models.CharField(max_length=1000, blank=True)
	CAS_NUMBER = models.CharField(max_length=1000, blank=True)
	CHEMICAL_NAME = models.CharField(max_length=1000, blank=True)
	CLASSIFICATION = models.CharField(max_length=1000, blank=True)
	UNIT_OF_MEASURE = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_1 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_2 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_3 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_4 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_5 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_6 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_7 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_8 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_9 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_10 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_11 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_12 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_13 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_14 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_15 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_16 = models.CharField(max_length=1000, blank=True)
	DIOXIN_DISTRIBUTION_17 = models.CharField(max_length=1000, blank=True)
	PRODUCE_THE_CHEMICAL = models.CharField(max_length=1000, blank=True)
	IMPORT_THE_CHEMICAL = models.CharField(max_length=1000, blank=True)
	ON_SITE_USE = models.CharField(max_length=1000, blank=True)
	SALE_OR_DISTRIBUTION = models.CharField(max_length=1000, blank=True)
	AS_A_BYPRODUCT = models.CharField(max_length=1000, blank=True)
	AS_A_MANUFACTURED_IMPURITY = models.CharField(max_length=1000, blank=True)
	AS_A_REACTANT = models.CharField(max_length=1000, blank=True)
	AS_A_FORMULATION_COMPONENT = models.CharField(max_length=1000, blank=True)
	AS_AN_ARTICLE_COMPONENT = models.CharField(max_length=1000, blank=True)
	REPACKAGING = models.CharField(max_length=1000, blank=True)
	AS_A_PROCESS_IMPURITY = models.CharField(max_length=1000, blank=True)
	AS_A_CHEMICAL_PROCESSING_AID = models.CharField(max_length=1000, blank=True)
	AS_A_MANUFACTURING_AID = models.CharField(max_length=1000, blank=True)
	ANCILLARY_OR_OTHER_USE = models.CharField(max_length=1000, blank=True)
	MAXIMUM_AMOUNT_ONSITE = models.CharField(max_length=1000, blank=True)
	FUGITIVE_AIR_EMISSIONS_TOTAL_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	FUGITIVE_AIR_EMISSIONS_TOTAL_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_FUGITIVE_AIR_EMISSIONS = models.CharField(max_length=1000, blank=True)
	FUGITIVE_OR_NON_POINT_AIR_EMISSIONS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	STACK_AIR_EMISSIONS_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	STACK_AIR_EMISSIONS_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_STACK_AIR_EMISSIONS = models.CharField(max_length=1000, blank=True)
	STACK_OR_POINT_AIR_EMISSIONS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	TOTAL_AIR_EMISSIONS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_A_STREAM_NAME = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_A_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_A_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_DISCHARGES_TO_STREAM_A = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_A_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_A_PERCENT_FROM_STORMWATER = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_B_STREAM_NAME = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_B_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_B_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_DISCHARGES_TO_STREAM_B = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_B_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_B_PERCENT_FROM_STORMWATER = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_C_STREAM_NAME = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_C_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_C_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_DISCHARGES_TO_STREAM_C = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_C_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_C_PERCENT_FROM_STORMWATER = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_D_STREAM_NAME = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_D_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_D_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_DISCHARGES_TO_STREAM_D = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_D_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_D_PERCENT_FROM_STORMWATER = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_E_STREAM_NAME = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_E_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_E_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_DISCHARGES_TO_STREAM_E = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_E_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_E_PERCENT_FROM_STORMWATER = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_F_STREAM_NAME = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_F_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_F_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_DISCHARGES_TO_STREAM_F = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_F_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	DISCHARGES_TO_STREAM_F_PERCENT_FROM_STORMWATER = models.CharField(max_length=1000, blank=True)
	TOTAL_NUMBER_OF_RECEIVING_STREAMS = models.CharField(max_length=1000, blank=True)
	TOTAL_SURFACE_WATER_DISCHARGE = models.CharField(max_length=1000, blank=True)
	UGRND_INJ_ONSITE_TO_CL_I_WELLS_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	UGRND_INJ_ONSITE_TO_CL_I_WELLS_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_UGRND_INJ_ONSITE_TO_CL_I_WELLS_POUNDS = models.CharField(max_length=1000, blank=True)
	UGRND_INJ_ONSITE_TO_CL_I_WELLS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_UGRND_INJ_ONSITE_TO_CL_II_V_WELLS_POUNDS = models.CharField(max_length=1000, blank=True)
	UNGRND_INJ_ONSITE_TO_CL_II_V_WELLS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	TOTAL_UNDERGROUND_INJECTION = models.CharField(max_length=1000, blank=True)
	RCRA_SUBTITLE_C_LANDFILLS_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	RCRA_SUBTITLE_C_LANDFILLS_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_RCRA_SUBTITLE_C_LANDFILLS = models.CharField(max_length=1000, blank=True)
	RCRA_SUBTITLE_C_LANDFILLS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	OTHER_LANDFILLS_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	OTHER_LANDFILLS_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_OTHER_ON_SITE_LAND_RELEASES = models.CharField(max_length=1000, blank=True)
	OTHER_LANDFILLS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	LAND_TRTMT_APPL_FARMING_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	LAND_TRTMT_APPL_FARMING_RELEASE_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_LAND_TREATMENT = models.CharField(max_length=1000, blank=True)
	LAND_TRTMT_APPL_FARMING_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	SURFACE_IMPOUNDMENT_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	SURFACE_IMPOUNDMENT_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_SURFACE_IMPOUNDMENTS = models.CharField(max_length=1000, blank=True)
	SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	OTHER_DISPOSAL_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	OTHER_DISPOSAL_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_OTHER_DISPOSAL = models.CharField(max_length=1000, blank=True)
	OTHER_DISPOSAL_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	TOTAL_ON_SITE_LAND_RELEASES = models.CharField(max_length=1000, blank=True)
	POTWS_TOTAL_TRANSFERS_METALS_ONLY = models.CharField(max_length=1000, blank=True)
	POTWS_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	STORAGE_ONLY = models.CharField(max_length=1000, blank=True)
	SOLIDIFICATION_STABILIZATION_METALS_AND_METAL_COMPOUNDS = models.CharField(max_length=1000, blank=True)
	WASTEWATER_TREATMENT_EXCLUDING_POTWS = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_POTWS_METALS_AND_METAL_COMPOUNDS = models.CharField(max_length=1000, blank=True)
	UNDERGROUND_INJECTION = models.CharField(max_length=1000, blank=True)
	LANDFILLS_DISPOSAL_SURFACE_IMPOUNDMENTS = models.CharField(max_length=1000, blank=True)
	SURFACE_IMPOUNDMENT = models.CharField(max_length=1000, blank=True)
	OTHER_LANDFILLS = models.CharField(max_length=1000, blank=True)
	RCRA_SUBTITLE_C_LANDFILSS = models.CharField(max_length=1000, blank=True)
	LAND_TREATMENT = models.CharField(max_length=1000, blank=True)
	OTHER_LAND_DISPOSAL = models.CharField(max_length=1000, blank=True)
	OTHER_OFF_SITE_MANAGEMENT = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_WASTE_BROKER_FOR_DISPOSAL = models.CharField(max_length=1000, blank=True)
	UNKNOWN = models.CharField(max_length=1000, blank=True)
	TOTAL_TRANSFERRED_OFF_SITE_TO_DISPOSAL = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_RECYCLING_M20_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_RECYCLING_M24_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_RECYCLING_M26_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_RECYCLING_M28_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_RECYCLING_M93_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_ENERGY_RECOVERY_M56_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_ENERGY_RECOVERY_M92_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_TREATMENT_M40_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_TREATMENT_M50_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_TREATMENT_M54_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_TREATMENT_M61_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_TREATMENT_M69_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_TREATMENT_M95_ONLY = models.CharField(max_length=1000, blank=True)
	TRANSFERS_TO_POTWS_NON_METALS = models.CharField(max_length=1000, blank=True)
	TOTAL_TRANSFERRED_OFF_SITE_FOR_FURTHER_WASTE_MANAGEMENT = models.CharField(max_length=1000, blank=True)
	ENERGY_RECOVERY_ONSITE_CURRENT_YEAR = models.CharField(max_length=1000, blank=True)
	QUANTITY_RECYCLED_ONSITE_CURRENT_YEAR = models.CharField(max_length=1000, blank=True)
	QUANTITY_TREATED_ONSITE_CURRENT_YEAR = models.CharField(max_length=1000, blank=True)
	OTHER_ON_SITE_WASTE_MANAGEMENT = models.CharField(max_length=1000, blank=True)
	ON_SITE_ENERGY_RECOVERY_METHOD_1 = models.CharField(max_length=1000, blank=True)
	ON_SITE_ENERGY_RECOVERY_METHOD_2 = models.CharField(max_length=1000, blank=True)
	ON_SITE_ENERGY_RECOVERY_METHOD_3 = models.CharField(max_length=1000, blank=True)
	ON_SITE_ENERGY_RECOVERY_METHOD_4 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_1 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_2 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_3 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_4 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_5 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_6 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_7 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_8 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_9 = models.CharField(max_length=1000, blank=True)
	ON_SITE_RECYCLING_PROCESSES_METHOD_10 = models.CharField(max_length=1000, blank=True)
	RCRA_C_SURFACE_IMPOUNDMENT_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	RCRA_C_SURFACE_IMPOUNDMENT_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_RCRA_C_SURFACE_IMPOUNDMENTS = models.CharField(max_length=1000, blank=True)
	RCRA_C_SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	OTHER_SURFACE_IMPOUNDMENT_RELEASE_POUNDS = models.CharField(max_length=1000, blank=True)
	OTHER_SURFACE_IMPOUNDMENT_RANGE_CODE = models.CharField(max_length=1000, blank=True)
	TOTAL_OTHER_SURFACE_IMPOUNDMENTS = models.CharField(max_length=1000, blank=True)
	OTHER_SURFACE_IMPOUNDMENT_BASIS_OF_ESTIMATE = models.CharField(max_length=1000, blank=True)
	RCRA_SUBTITLE_C_SURFACE_IMPOUNDMENTS_M66 = models.CharField(max_length=1000, blank=True)
	OTHER_SURFACE_IMPOUNDMENTS_M67 = models.CharField(max_length=1000, blank=True)
	UNDERGROUND_INJECTION_TO_CLASS_I_WELLS_M81 = models.CharField(max_length=1000, blank=True)
	UNDERGROUND_INJECTION_TO_CLASS_II_V_WELLS_M82 = models.CharField(max_length=1000, blank=True)
	ASSIGNED_FED_FACILITY_FLAG = models.CharField(max_length=1000, blank=True)
	PUBLIC_CONTACT_EMAIL = models.CharField(max_length=1000, blank=True)
	REVISION_CODE_1 = models.CharField(max_length=1000, blank=True)
	REVISION_CODE_2 = models.CharField(max_length=1000, blank=True)
	METAL_INDICATOR = models.CharField(max_length=1000, blank=True)

	def __unicode__(self):
		predence_of_emissions = [
			self.TOTAL_ON_SITE_LAND_RELEASES, 
			self.TOTAL_AIR_EMISSIONS, 
			self.TOTAL_OTHER_DISPOSAL, 
			self.TOTAL_SURFACE_IMPOUNDMENTS, 
			self.TOTAL_UNDERGROUND_INJECTION, 
			self.TOTAL_LAND_TREATMENT, 
			self.TOTAL_SURFACE_WATER_DISCHARGE, 
			self.TOTAL_FUGITIVE_AIR_EMISSIONS
		]

		val = next((x for x in predence_of_emissions if x != "0"), "0")
		return val + " " + self.UNIT_OF_MEASURE + " " + self.CHEMICAL_NAME
