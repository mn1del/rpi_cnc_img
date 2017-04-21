# feeds_speeds.py
# stores generic recommended min/max chiploads by material and bit diameter
# Calculates RPM for given feed rate, and vice versa.


# list of spindle diameters
diams = [3.175, 6.35, 9.525, 12.7]

# populate chipload dictionaries
hardwood = {
        "min" : {"diam":diams, "chipload":[0.0762, 0.2286, 0.381, 0.4826]},
        "max" : {"diam":diams, "chipload":[0.127, 0.2794, 0.4572, 0.5334]}}

softply = {
        "min" : {"diam":diams, "chipload":[0.1016, 0.2794, 0.4318, 0.5334]},
        "max" : {"diam":diams, "chipload":[0.1524, 0.3302, 0.508, 0.5842]}}

mdf = {
        "min" : {"diam":diams, "chipload":[0.1016, 0.3302, 0.508, 0.635]},
        "max" : {"diam":diams, "chipload":[0.1778, 0.4064, 0.5842, 0.6858]}}

lam = {
        "min" : {"diam":diams, "chipload":[0.0762, 0.2286, 0.381, 0.5842]},
        "max" : {"diam":diams, "chipload":[0.127, 0.3048, 0.4572, 0.635]}}

phen = {
        "min" : {"diam":diams, "chipload":[0.1016, 0.2794, 0.4318, 0.6096]},
        "max" : {"diam":diams, "chipload":[0.127, 0.3048, 0.4572, 0.6604]}}

plastic_hard = {
        "min" : {"diam":diams, "chipload":[0.0508, 0.1524, 0.2032, 0.254]},
        "max" : {"diam":diams, "chipload":[ 0.1016, 0.2286, 0.254, 0.3048]}}

plastic_soft = {
        "min" : {"diam":diams, "chipload":[0.0762, 0.1778, 0.254, 0.3048]},
        "max" : {"diam":diams, "chipload":[0.1524, 0.254, 0.3048, 0.4064]}}

solid_surface = {
        "min" : {"diam":diams, "chipload":[0.0508, 0.1524, 0.2032, 0.254]},
        "max" : {"diam":diams, "chipload":[0.1016, 0.2286, 0.254, 0.3048]}}

acrylic = {
        "min" : {"diam":diams, "chipload":[0.0762, 0.2032, 0.254, 0.3048]},
        "max" : {"diam":diams, "chipload":[0.127, 0.254, 0.3048, 0.381]}}

aluminium = {
        "min" : {"diam":diams, "chipload":[0.0762, 0.127, 0.1524, 0.2032]},
        "max" : {"diam":diams, "chipload":[0.127, 0.1778, 0.2032, 0.254]}}

def rpm_max(cutterDiam=6, numFlutes=2 material=hardwood, feedRate=750):
    s = InterpolatedUnivariateSpline(material["min"]["diam"], material["min"]["chipload"],k=1)
    chipload = s(cutterDiam)
    return feedRate/(numFlutes*chipload)
