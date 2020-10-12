#!/usr/bin/python3
'''This script is a graphic user interface using for generating KML files and CSV files.'''
import sys
import traceback

try:
    import convert
    import tkinter as tk 
    from tkinter import ttk 
    
    
   
    
    
    
    def ssconvert():  
        in_crs = incrs.get()
        out_crs = outcrs.get()
        in_x = x_var.get()
        in_y = y_var.get()
        conversion = convert.SalishSeaCoordConverter(incrs.get(), outcrs.get(), x_var.get() , y_var.get())
        
        #out_label = Label(root, text= str(conversion.out_x) +', ' +str( conversion.out_y))
        #out_latel.pack()
        return print (conversion.out_x, conversion.out_y)
    
    # Creating tkinter window 
    window = tk.Tk() 
    window.title('Salish Sea Coordinate Converter') 
    window.geometry('400x200') 
    
    # label 
    ttk.Label(window, text = "Select input CRS :").grid(column = 0, row = 5, padx = 5, pady = 10) 
    # label 
    ttk.Label(window, text = "Select output CRS :").grid(column = 0, row = 6, padx = 5, pady = 10) 
    # label 
    ttk.Label(window, text = "x :").grid(column = 0, row = 7, padx = 5, pady = 10) 
    # label 
    ttk.Label(window, text = "y :").grid(column = 0, row = 8, padx = 5, pady = 10)     
    
    
    # Combobox creation 
    incrs = tk.StringVar() 
    crschoosen = ttk.Combobox(window, width = 15, textvariable = incrs)
    # Combobox creation 
    outcrs = tk.StringVar() 
    crschoosen2 = ttk.Combobox(window, width = 15, textvariable = outcrs) 
    
    x_var = tk.DoubleVar() 
    x_entry = tk.Entry(window, textvariable = x_var) 
    y_var = tk.DoubleVar() 
    y_entry = tk.Entry(window, textvariable = y_var)    
    
    # Adding combobox drop down list 
    crschoosen['values'] = ('WN_HARN','WN_NAD83','WN_NAD27','WS_HARN','WS_NAD83','WS_NAD27','UTM10N_WGS84','UTM10N_NAD83','UTM10N_NAD27','UTM10N_WGS72','UTM10N_HARN','WGS84','WGS72') 
    crschoosen2['values'] = ('WN_HARN','WN_NAD83','WN_NAD27','WS_HARN','WS_NAD83','WS_NAD27','UTM10N_WGS84','UTM10N_NAD83','UTM10N_NAD27','UTM10N_WGS72','UTM10N_HARN','WGS84','WGS72') 
    crschoosen.grid(column = 1, row = 5) 
    crschoosen2.grid(column = 1, row = 6) 
    crschoosen.current() 
    crschoosen2.current() 
    
    
    x_entry.grid(row=7,column=1) 
    y_entry.grid(row=8,column=1) 
    
    
    sub_btn=tk.Button(window,text = 'Convert', command = ssconvert)
    
    sub_btn.grid(row=9,column=1) 
    
    
    
    
    window.mainloop() 


except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))