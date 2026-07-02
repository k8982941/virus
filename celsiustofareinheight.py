def convertor(val, input, output):
    if input.upper()=="C" and output.upper()=="F":
        gejor=val*1.8+32
    elif input.upper()=="F" and output.upper()=="C":
        gejor=(val-32)/1.8
    elif input.upper()=="K" and output.upper()=="C":
        gejor=val-273.15
    elif input.upper()=="K" and output.upper()=="F":
        gejor=1.8*val-459.67
    elif input.upper()=="C" and output.upper()=="K":
        gejor=val+273.15
    elif input.upper()=="F" and output.upper()=="K":
        gejor=(val+459.67)/1.8
    else:
        gejor="シックス・セブン・オハイオ・スキビディ・トイレ"
    gejor=round(gejor,3)
    return gejor

print(convertor(99,"f",'c'))