# feeds_speeds.py
# stores generic recommended min/max chiploads by material and bit diameter
# Calculates RPM for given feed rate, and vice versa.


# define min/max chipload empty dictionary
cl_min = {}
cl_max = {}

# list of spindle diameters
diams = [3.175, 6.35, 9.525, 12.7]

# populate il chipload dictionaries
hardwood = {}
hardwood["min"] = {
            diams[0]:0.0762,
            diams[1]:0.2286,
            diams[2]:0.381,
            diams[3]:0.4826
        }
hardwood["max"] = {
            diams[0]:0.127,
            diams[1]:0.2794,
            diams[2]:0.4572,
            diams[3]:0.5334
        }

softply = {}
softply["min"] = {
            diams[0]:0.1016,
            diams[1]:0.2794,
            diams[2]:0.4318,
            diams[3]:0.5334
        }
softply["max"] = {
            diams[0]:0.1524,
            diams[1]:0.3302,
            diams[2]:0.508,
            diams[3]:0.5842
        }

mdf = {}
mdf["min"] = {
            diams[0]:0.1016,
            diams[1]:0.3302,
            diams[2]:0.508,
            diams[3]:0.635
        }
mdf["max"] = {
            diams[0]:0.1778,
            diams[1]:0.4064,
            diams[2]:0.5842,
            diams[3]:0.6858
        }

lam = {}
lam["min"] = {
            diams[0]:0.0762,
            diams[1]:0.2286,
            diams[2]:0.381,
            diams[3]:0.5842
        }
lam["max"] = {
            diams[0]:0.127,
            diams[1]:0.3048,
            diams[2]:0.4572,
            diams[3]:0.635
        }

phen = {}
phen["min"] = {
            diams[0]:0.1016,
            diams[1]:0.2794,
            diams[2]:0.4318,
            diams[3]:0.6096
        }
phen["max"] = {
            diams[0]:0.127,
            diams[1]:0.3048,
            diams[2]:0.4572,
            diams[3]:0.6604
        }
plastic_hard = {}
plastic_hard["min"] = {
            diams[0]:0.0508,
            diams[1]:0.1524,
            diams[2]:0.2032,
            diams[3]:0.254
        }
plastic_hard["max"] = {
            diams[0]:0.1016,
            diams[1]:0.2286,
            diams[2]:0.254,
            diams[3]:0.3048
        }

plastic_soft = {}
plastic_soft["min"] = {
            diams[0]:0.0762,
            diams[1]:0.1778,
            diams[2]:0.254,
            diams[3]:0.3048
        }
plastic_soft["max"] = {
            diams[0]:0.1524,
            diams[1]:0.254,
            diams[2]:0.3048,
            diams[3]:0.4064
        }

solid_surface = {}
solid_surface["min"] = {
            diams[0]:0.0508,
            diams[1]:0.1524,
            diams[2]:0.2032,
            diams[3]:0.254
        }
solid_surface["max"] = {
            diams[0]:0.1016,
            diams[1]:0.2286,
            diams[2]:0.254,
            diams[3]:0.3048
        }

acrylic = {
    "min" : {
        diams[0]:0.0762,
        diams[1]:0.2032,
        diams[2]:0.254,
        diams[3]:0.3048
    },
    "max" : {
        diams[0]:0.127,
        diams[1]:0.254,
        diams[2]:0.3048,
        diams[3]:0.381
    }}

aluminium = {
    "min" : {
        diams[0]:0.0762,
        diams[1]:0.127,
        diams[2]:0.1524,
        diams[3]:0.2032
    },
    "max" : {
        diams[0]:0.127,
        diams[1]:0.1778,
        diams[2]:0.2032,
        diams[3]:0.254
    }}
