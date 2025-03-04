# -*- coding: utf-8 -*-
"""
This module returns the constants of the code inclduing the info of sets and
parameter filese
"""


def take_trade_ids(mode):
    """
    Creates a dictionary for storing the information of the parameter sheets of 
    inter-regional link data based on the given mode
    """

    trade_data_ids = {
        "line_fixed_cost": {"sheet_name": "F_OM", "index_col": 0, "header": [0, 1]},
        "line_var_cost": {"sheet_name": "V_OM", "index_col": 0, "header": [0, 1]},
        "line_residual_cap": {
            "sheet_name": "Residual_capacity",
            "index_col": 0,
            "header": [0, 1],
        },
        "line_eff": {"sheet_name": "Line_efficiency", "index_col": 0, "header": [0, 1]},
        "line_capacity_factor": {
            "sheet_name": "Capacity_factor_line",
            "index_col": 0,
            "header": [0, 1],
        },
        "annualprod_per_unitcapacity": {
            "sheet_name": "AnnualProd_perunit_capacity",
            "index_col": 0,
            "header": [0, 1],
        },
    }

    if mode == "Planning":

        trade_data_ids.update(
            {
                "line_inv": {"sheet_name": "INV", "index_col": 0, "header": [0, 1]},
                "line_decom_cost": {
                    "sheet_name": "Decom_cost",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "line_mintotcap": {
                    "sheet_name": "Min_totalcap",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "line_maxtotcap": {
                    "sheet_name": "Max_totalcap",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "line_min_newcap": {
                    "sheet_name": "Min_newcap",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "line_max_newcap": {
                    "sheet_name": "Max_newcap",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "line_lifetime": {
                    "sheet_name": "Line_lifetime",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "line_economic_lifetime": {
                    "sheet_name": "Line_Economic_life",
                    "index_col": 0,
                    "header": [0, 1],
                },
                "interest_rate": {
                    "sheet_name": "Interest_rate",
                    "index_col": 0,
                    "header": [0, 1],
                },
            }
        )

    return trade_data_ids


def take_global_ids(mode):
    """
    Creates a dictionary for storing the information of the parameter sheets of 
    global data based on the given mode
    """
    global_data_ids = {
        "global_min_production": {
            "sheet_name": "Min_production_global",
            "index_col": 0,
            "header": 0,
        },
        "global_max_production": {
            "sheet_name": "Max_production_global",
            "index_col": 0,
            "header": 0,
        },
        "global_emission_cap_annual": {
            "sheet_name": "Glob_emission_cap_annual",
            "index_col": 0,
            "header": 0,
        },
    }

    if mode == "Planning":

        global_data_ids.update(
            {
                "global_mintotcap": {
                    "sheet_name": "Min_totalcap_global",
                    "index_col": 0,
                    "header": 0,
                },
                "global_maxtotcap": {
                    "sheet_name": "Max_totalcap_global",
                    "index_col": 0,
                    "header": 0,
                },
                "global_min_newcap": {
                    "sheet_name": "Min_newcap_global",
                    "index_col": 0,
                    "header": 0,
                },
                "global_max_newcap": {
                    "sheet_name": "Max_newcap_global",
                    "index_col": 0,
                    "header": 0,
                },
                "global_discount_rate": {
                    "sheet_name": "Discount_rate",
                    "index_col": 0,
                    "header": 0,
                },
            }
        )

    return global_data_ids


# Constants of parameters_regions data


def take_ids(regions, technologies, mode):

    """
    Creates a dictionary for storing the information of the parameter sheets of 
    regional data based on the given mode and the list of regions and technologies
    within each region
    """
    regional_data_ids = {}
    for reg in regions:
        regional_data_ids[reg] = {
            "tech_fixed_cost": {"sheet_name": "F_OM", "index_col": 0, "header": [0, 1]},
            "tech_var_cost": {"sheet_name": "V_OM", "index_col": 0, "header": [0, 1]},
            "tech_residual_cap": {
                "sheet_name": "Residual_capacity",
                "index_col": 0,
                "header": [0, 1],
            },
            "tech_max_production": {
                "sheet_name": "Max_production",
                "index_col": 0,
                "header": [0, 1],
            },
            "tech_min_production": {
                "sheet_name": "Min_production",
                "index_col": 0,
                "header": [0, 1],
            },
            "tech_max_production_h": {
                "sheet_name": "Max_production_h",
                "index_col": [0, 1],
                "header": [0, 1],
            },
            "tech_min_production_h": {
                "sheet_name": "Min_production_h",
                "index_col": [0, 1],
                "header": [0, 1],
            },
            "annualprod_per_unitcapacity": {
                "sheet_name": "AnnualProd_perunit_capacity",
                "index_col": 0,
                "header": [0, 1],
            },
            "tech_efficiency": {
                "sheet_name": "Tech_efficiency",
                "index_col": 0,
                "header": [0, 1],
            },
            "tech_capacity_factor": {
                "sheet_name": "Capacity_factor_tech",
                "index_col": 0,
                "header": [0, 1],
            },
            "specific_emission": {
                "sheet_name": "Specific_emission",
                "index_col": 0,
                "header": [0, 1],
            },
            "carbon_tax": {
                "sheet_name": "Carbon_tax",
                "index_col": 0,
                "header": [0, 1],
            },
            "fix_taxsub": {
                "sheet_name": "Fix_taxsub",
                "index_col": 0,
                "header": [0, 1, 2],
            },
            "demand": {"sheet_name": "Demand", "index_col": [0, 1], "header": 0},
            "res_capacity_factor": {
                "sheet_name": "capacity_factor_resource",
                "index_col": [0, 1],
                "header": [0, 1],
            },
            "emission_cap_annual": {
                "sheet_name": "Emission_cap_annual",
                "index_col": 0,
                "header": 0,
            },
        }

        if mode == "Planning":

            regional_data_ids[reg].update(
                {
                    "tech_inv": {"sheet_name": "INV", "index_col": 0, "header": [0, 1]},
                    "tech_decom_cost": {
                        "sheet_name": "Decom_cost",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "tech_mintotcap": {
                        "sheet_name": "Min_totalcap",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "tech_maxtotcap": {
                        "sheet_name": "Max_totalcap",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "tech_min_newcap": {
                        "sheet_name": "Min_newcap",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "tech_max_newcap": {
                        "sheet_name": "Max_newcap",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "tech_lifetime": {
                        "sheet_name": "Tech_lifetime",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "economic_lifetime": {
                        "sheet_name": "Economic_lifetime",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "interest_rate": {
                        "sheet_name": "Interest_rate",
                        "index_col": 0,
                        "header": [0, 1],
                    },
                    "inv_taxsub": {
                        "sheet_name": "Investment_taxsub",
                        "index_col": 0,
                        "header": [0, 1, 2],
                    },
                    "discount_rate": {
                        "sheet_name": "Discount_rate",
                        "index_col": 0,
                        "header": 0,
                    },
                }
            )

        if "Conversion_plus" in technologies[reg].keys():

            regional_data_ids[reg].update(
                {
                    "carrier_ratio_in": {
                        "sheet_name": "Carrier_ratio_in",
                        "index_col": [0, 1],
                        "header": [0, 1],
                    },
                    "carrier_ratio_out": {
                        "sheet_name": "Carrier_ratio_out",
                        "index_col": [0, 1],
                        "header": [0, 1],
                    },
                }
            )

        if "Storage" in technologies[reg].keys():

            regional_data_ids[reg].update(
                {
                    "storage_charge_efficiency": {
                        "sheet_name": "Storage_charge_efficiency",
                        "index_col": 0,
                        "header": 0,
                    },
                    "storage_discharge_efficiency": {
                        "sheet_name": "Storage_discharge_efficiency",
                        "index_col": 0,
                        "header": 0,
                    },
                    "storage_min_SOC": {
                        "sheet_name": "Storage_min_SOC",
                        "index_col": 0,
                        "header": 0,
                    },
                    "storage_initial_SOC": {
                        "sheet_name": "Storage_initial_SOC",
                        "index_col": 0,
                        "header": 0,
                    },
                    "storage_charge_time": {
                        "sheet_name": "Storage_charge_time",
                        "index_col": 0,
                        "header": 0,
                    },
                    "storage_discharge_time": {
                        "sheet_name": "Storage_discharge_time",
                        "index_col": 0,
                        "header": 0,
                    },
                }
            )

    return regional_data_ids


# Constants of input set tables

global_set_ids = {
    "Regions": ["Region", "Region_name"],
    "Years": ["Year", "Year_name"],
    "Timesteps": ["Timeslice", "Timeslice_name", "Timeslice_fraction"],
    "Time_horizon": ["Start", "End"],
    "Carriers_glob": ["Carrier", "Carr_name", "Carr_type"],
    "Technologies_glob": ["Technology", "Tech_name", "Tech_category"],
}


regional_set_ids = {
    "Technologies": ["Technology", "Tech_name", "Tech_category"],
    "Carriers": ["Carrier", "Carr_name", "Carr_type"],
    "Carrier_input": ["Technology", "Carrier_in"],
    "Carrier_output": ["Technology", "Carrier_out"],
}

technology_categories = [
    "Supply",
    "Conversion",
    "Conversion_plus",
    "Transmission",
    "Demand",
    "Storage",
]

carrier_types = ["Resource", "Intermediate", "Demand"]
