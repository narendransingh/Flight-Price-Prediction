from flask import Flask, request, render_template
from flask_cors import cross_origin
#import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_price_RF_updated.pk1", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Start Date
        date_dept = request.form["Dept_Date_Time"]
        Journey_day = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dept, format ="%Y-%m-%dT%H:%M").month)

        # Start Time
        dep_time_hrs = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").hour)
        dep_time_mins = int(pd.to_datetime(date_dept, format="%Y-%m-%dT%H:%M").minute)

        # Arrival Date Time
        date_arrival = request.form["Arrival_Date_Time"]
        arr_time_hrs = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").hour)
        arr_time_mins = int(pd.to_datetime(date_arrival, format="%Y-%m-%dT%H:%M").minute)

        if (dep_time_hrs < arr_time_hrs):
            duration_hrs = abs(arr_time_hrs-dep_time_hrs)
        else:
            duration_hrs = (24 - dep_time_hrs)+arr_time_hrs

        duration_mins = abs(arr_time_mins - dep_time_mins)

        #airline selection
        airline = request.form["Airlines"]
        if(airline == 'Jet_Airways'):
            Airline_Jet_Airways = 1
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline == 'IndiGo'):
            Airline_Jet_Airways = 0
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 1
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline == 'Air_India'):
            Airline_Jet_Airways = 0
            Airline_Air_India = 1
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline == 'SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline == 'Vistara'):
            Airline_Jet_Airways = 0
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline == 'Go_Air'):
            Airline_Jet_Airways = 0
            Airline_Air_India = 0
            Airline_GoAir = 1
            Airline_IndiGo = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        else:
            Airline_Jet_Airways = 0
            Airline_Air_India = 0
            Airline_GoAir = 0
            Airline_IndiGo = 0
            Airline_Jet_Airways_Business = 0
            Airline_Multiple_carriers = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        # source selection
        source = request.form["Source"]
        if (source == 'Delhi'):
            Source_BOM = 0
            Source_CCU = 0
            Source_DEL = 1
            Source_MAA = 0

        elif (source == 'Kolkata'):
            Source_BOM = 0
            Source_CCU = 1
            Source_DEL = 0
            Source_MAA = 0

        elif (source == 'Mumbai'):
            Source_BOM = 1
            Source_CCU = 0
            Source_DEL = 0
            Source_MAA = 0

        elif (source == 'Chennai'):
            Source_BOM = 0
            Source_CCU = 0
            Source_DEL = 0
            Source_MAA = 1

        else:
            Source_BOM = 0
            Source_CCU = 0
            Source_DEL = 0
            Source_MAA = 0

        # destination selection
        destination = request.form["Destination"]
        if (destination == 'Delhi'):
            Destination_CCU = 0
            Destination_COK = 0
            Destination_DEL = 1
            Destination_HYD = 0

        elif (destination == 'Cochin'):
            Destination_CCU = 0
            Destination_COK = 1
            Destination_DEL = 0
            Destination_HYD = 0

        elif (destination == 'Kolkata'):
            Destination_CCU = 1
            Destination_COK = 0
            Destination_DEL = 0
            Destination_HYD = 0

        elif (destination == 'Hyderabad'):
            Destination_CCU = 0
            Destination_COK = 0
            Destination_DEL = 0
            Destination_HYD = 1

        else:
            Destination_CCU = 0
            Destination_COK = 0
            Destination_DEL = 0
            Destination_HYD = 0

        #stops
        Total_Stops = (request.form['Stops'])
        if (Total_Stops == '0'):
            Stop1_AMD = 0
            Stop1_ATQ = 0
            Stop1_BBI = 0
            Stop1_BDQ = 0
            Stop1_BHO = 0
            Stop1_BLR = 0
            Stop1_BOM = 0
            Stop1_CCU = 0
            Stop1_COK = 0
            Stop1_DED = 0
            Stop1_DEL = 0
            Stop1_GAU = 0
            Stop1_GOI = 0
            Stop1_GWL = 0
            Stop1_HBX = 0
            Stop1_HYD = 0
            Stop1_IDR = 0
            Stop1_IXA = 0
            Stop1_IXB = 0
            Stop1_IXC = 0
            Stop1_IXR = 0
            Stop1_IXU = 0
            Stop1_IXZ = 0
            Stop1_JAI = 0
            Stop1_JDH = 0
            Stop1_JLR = 0
            Stop1_KNU = 0
            Stop1_LKO = 0
            Stop1_MAA = 0
            Stop1_NAG = 0
            Stop1_NDC = 0
            Stop1_PAT = 0
            Stop1_PNQ = 0
            Stop1_RPR = 0
            Stop1_STV = 0
            Stop1_TRV = 0
            Stop1_UDR = 0
            Stop1_VGA = 0
            Stop1_VNS = 0
            Stop1_VTZ = 0
            Stop2_AMD = 0
            Stop2_BBI = 0
            Stop2_BHO = 0
            Stop2_BOM = 0
            Stop2_CCU = 0
            Stop2_COK = 0
            Stop2_DEL = 0
            Stop2_GAU = 0
            Stop2_GOI = 0
            Stop2_HBX = 0
            Stop2_HYD = 0
            Stop2_IDR = 0
            Stop2_IMF = 0
            Stop2_ISK = 0
            Stop2_IXC = 0
            Stop2_IXR = 0
            Stop2_JAI = 0
            Stop2_JDH = 0
            Stop2_MAA = 0
            Stop2_NAG = 0
            Stop2_PNQ = 0
            Stop2_TRV = 0
            Stop2_UDR = 0
            Stop2_VGA = 0
            Stop2_VTZ = 0
            Stop3_AMD = 0
            Stop3_BBI = 0
            Stop3_BHO = 0
            Stop3_BOM = 0
            Stop3_DEL = 0
            Stop3_GWL = 0
            Stop3_HYD = 0
            Stop3_NAG = 0
            Stop3_TRV = 0

        if (Total_Stops == '1'):
            Stop1_AMD = 1
            Stop1_ATQ = 0
            Stop1_BBI = 0
            Stop1_BDQ = 0
            Stop1_BHO = 0
            Stop1_BLR = 0
            Stop1_BOM = 1
            Stop1_CCU = 0
            Stop1_COK = 0
            Stop1_DED = 0
            Stop1_DEL = 1
            Stop1_GAU = 0
            Stop1_GOI = 0
            Stop1_GWL = 0
            Stop1_HBX = 0
            Stop1_HYD = 0
            Stop1_IDR = 0
            Stop1_IXA = 0
            Stop1_IXB = 0
            Stop1_IXC = 0
            Stop1_IXR = 0
            Stop1_IXU = 0
            Stop1_IXZ = 0
            Stop1_JAI = 0
            Stop1_JDH = 1
            Stop1_JLR = 0
            Stop1_KNU = 0
            Stop1_LKO = 0
            Stop1_MAA = 0
            Stop1_NAG = 0
            Stop1_NDC = 0
            Stop1_PAT = 0
            Stop1_PNQ = 0
            Stop1_RPR = 0
            Stop1_STV = 0
            Stop1_TRV = 0
            Stop1_UDR = 0
            Stop1_VGA = 0
            Stop1_VNS = 0
            Stop1_VTZ = 0
            Stop2_AMD = 0
            Stop2_BBI = 0
            Stop2_BHO = 0
            Stop2_BOM = 0
            Stop2_CCU = 0
            Stop2_COK = 0
            Stop2_DEL = 0
            Stop2_GAU = 0
            Stop2_GOI = 0
            Stop2_HBX = 0
            Stop2_HYD = 0
            Stop2_IDR = 0
            Stop2_IMF = 0
            Stop2_ISK = 0
            Stop2_IXC = 0
            Stop2_IXR = 0
            Stop2_JAI = 0
            Stop2_JDH = 0
            Stop2_MAA = 0
            Stop2_NAG = 0
            Stop2_PNQ = 0
            Stop2_TRV = 0
            Stop2_UDR = 0
            Stop2_VGA = 0
            Stop2_VTZ = 0
            Stop3_AMD = 0
            Stop3_BBI = 0
            Stop3_BHO = 0
            Stop3_BOM = 0
            Stop3_DEL = 0
            Stop3_GWL = 0
            Stop3_HYD = 0
            Stop3_NAG = 0
            Stop3_TRV = 0

        if (Total_Stops == '2'):
            Stop1_AMD = 0
            Stop1_ATQ = 0
            Stop1_BBI = 0
            Stop1_BDQ = 0
            Stop1_BHO = 0
            Stop1_BLR = 0
            Stop1_BOM = 0
            Stop1_CCU = 0
            Stop1_COK = 0
            Stop1_DED = 0
            Stop1_DEL = 0
            Stop1_GAU = 0
            Stop1_GOI = 0
            Stop1_GWL = 0
            Stop1_HBX = 0
            Stop1_HYD = 0
            Stop1_IDR = 0
            Stop1_IXA = 0
            Stop1_IXB = 0
            Stop1_IXC = 0
            Stop1_IXR = 0
            Stop1_IXU = 0
            Stop1_IXZ = 0
            Stop1_JAI = 0
            Stop1_JDH = 0
            Stop1_JLR = 0
            Stop1_KNU = 0
            Stop1_LKO = 0
            Stop1_MAA = 0
            Stop1_NAG = 0
            Stop1_NDC = 0
            Stop1_PAT = 0
            Stop1_PNQ = 0
            Stop1_RPR = 0
            Stop1_STV = 0
            Stop1_TRV = 0
            Stop1_UDR = 0
            Stop1_VGA = 0
            Stop1_VNS = 0
            Stop1_VTZ = 0
            Stop2_AMD = 0
            Stop2_BBI = 0
            Stop2_BHO = 0
            Stop2_BOM = 1
            Stop2_CCU = 0
            Stop2_COK = 0
            Stop2_DEL = 1
            Stop2_GAU = 0
            Stop2_GOI = 0
            Stop2_HBX = 0
            Stop2_HYD = 1
            Stop2_IDR = 0
            Stop2_IMF = 0
            Stop2_ISK = 0
            Stop2_IXC = 0
            Stop2_IXR = 0
            Stop2_JAI = 0
            Stop2_JDH = 0
            Stop2_MAA = 1
            Stop2_NAG = 0
            Stop2_PNQ = 0
            Stop2_TRV = 0
            Stop2_UDR = 0
            Stop2_VGA = 0
            Stop2_VTZ = 0
            Stop3_AMD = 0
            Stop3_BBI = 0
            Stop3_BHO = 0
            Stop3_BOM = 0
            Stop3_DEL = 0
            Stop3_GWL = 0
            Stop3_HYD = 0
            Stop3_NAG = 0
            Stop3_TRV = 0

        if (Total_Stops == '3'):
            Stop1_AMD = 0
            Stop1_ATQ = 0
            Stop1_BBI = 0
            Stop1_BDQ = 0
            Stop1_BHO = 0
            Stop1_BLR = 0
            Stop1_BOM = 0
            Stop1_CCU = 0
            Stop1_COK = 0
            Stop1_DED = 0
            Stop1_DEL = 0
            Stop1_GAU = 0
            Stop1_GOI = 0
            Stop1_GWL = 0
            Stop1_HBX = 0
            Stop1_HYD = 0
            Stop1_IDR = 0
            Stop1_IXA = 0
            Stop1_IXB = 0
            Stop1_IXC = 0
            Stop1_IXR = 0
            Stop1_IXU = 0
            Stop1_IXZ = 0
            Stop1_JAI = 0
            Stop1_JDH = 0
            Stop1_JLR = 0
            Stop1_KNU = 0
            Stop1_LKO = 0
            Stop1_MAA = 0
            Stop1_NAG = 0
            Stop1_NDC = 0
            Stop1_PAT = 0
            Stop1_PNQ = 0
            Stop1_RPR = 0
            Stop1_STV = 0
            Stop1_TRV = 0
            Stop1_UDR = 0
            Stop1_VGA = 0
            Stop1_VNS = 0
            Stop1_VTZ = 0
            Stop2_AMD = 0
            Stop2_BBI = 0
            Stop2_BHO = 0
            Stop2_BOM = 0
            Stop2_CCU = 0
            Stop2_COK = 0
            Stop2_DEL = 0
            Stop2_GAU = 0
            Stop2_GOI = 0
            Stop2_HBX = 0
            Stop2_HYD = 0
            Stop2_IDR = 0
            Stop2_IMF = 0
            Stop2_ISK = 0
            Stop2_IXC = 0
            Stop2_IXR = 0
            Stop2_JAI = 0
            Stop2_JDH = 0
            Stop2_MAA = 0
            Stop2_NAG = 0
            Stop2_PNQ = 0
            Stop2_TRV = 0
            Stop2_UDR = 0
            Stop2_VGA = 0
            Stop2_VTZ = 0
            Stop3_AMD = 0
            Stop3_BBI = 0
            Stop3_BHO = 0
            Stop3_BOM = 1
            Stop3_DEL = 1
            Stop3_GWL = 0
            Stop3_HYD = 0
            Stop3_NAG = 0
            Stop3_TRV = 0


    prediction = model.predict([[Total_Stops, Journey_day, Journey_month, dep_time_hrs,
                                 dep_time_mins, arr_time_hrs, arr_time_mins, duration_hrs,
                                 duration_mins, Airline_Air_India, Airline_GoAir, Airline_IndiGo,
                                 Airline_Jet_Airways, Airline_Jet_Airways_Business,
                                 Airline_Multiple_carriers, Airline_Multiple_carriers_Premium_economy,
                                 Airline_SpiceJet, Airline_Vistara,
                                 Airline_Vistara_Premium_economy, Source_BOM, Source_CCU, Source_DEL,
                                 Source_MAA, Destination_CCU, Destination_COK, Destination_DEL,
                                 Destination_HYD, Stop1_AMD, Stop1_ATQ, Stop1_BBI, Stop1_BDQ,
                                 Stop1_BHO, Stop1_BLR, Stop1_BOM, Stop1_CCU, Stop1_COK, Stop1_DED,
                                 Stop1_DEL, Stop1_GAU, Stop1_GOI, Stop1_GWL, Stop1_HBX, Stop1_HYD,
                                 Stop1_IDR, Stop1_IXA, Stop1_IXB, Stop1_IXC, Stop1_IXR, Stop1_IXU,
                                 Stop1_IXZ, Stop1_JAI, Stop1_JDH, Stop1_JLR, Stop1_KNU, Stop1_LKO,
                                 Stop1_MAA, Stop1_NAG, Stop1_NDC, Stop1_PAT, Stop1_PNQ, Stop1_RPR,
                                 Stop1_STV, Stop1_TRV, Stop1_UDR, Stop1_VGA, Stop1_VNS, Stop1_VTZ,
                                 Stop2_AMD, Stop2_BBI, Stop2_BHO, Stop2_BOM, Stop2_CCU, Stop2_COK,
                                 Stop2_DEL, Stop2_GAU, Stop2_GOI, Stop2_HBX, Stop2_HYD, Stop2_IDR,
                                 Stop2_IMF, Stop2_ISK, Stop2_IXC, Stop2_IXR, Stop2_JAI, Stop2_JDH,
                                 Stop2_MAA, Stop2_NAG, Stop2_PNQ, Stop2_TRV, Stop2_UDR, Stop2_VGA,
                                 Stop2_VTZ, Stop3_AMD, Stop3_BBI, Stop3_BHO, Stop3_BOM, Stop3_DEL,
                                 Stop3_GWL, Stop3_HYD, Stop3_NAG, Stop3_TRV]])


    output = round(prediction[0],2)

    return render_template('home.html',
                           prediction_text="Your predicted flight price from {} to {} is Rs. {:,}".format(source, destination, output))


    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)