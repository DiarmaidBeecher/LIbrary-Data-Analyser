# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:36:06 2022
Student ID: A00303539

@author: Diarmaid Beecher
"""
import matplotlib.pyplot as plt
from math import sqrt

def calc_mean(nums):
    """
    Calculates the mean of a list of numbers

    Parameters
    ----------
    nums : int
        The list of numbers for which the mean is to be calculated

    Returns
    -------
    mean : float
        The mean of the list of numbers 

    """
    mean = sum(nums)/len(nums)
    return mean

def calc_median(nums):
    """
    Calculates the median of a list of numbers

    Parameters
    ----------
    nums : int
        The list of numbers for which the median is to be calculated

    Returns
    -------
    median : int
        The median of the list of numbers

    """
    sorted_nums = sorted(nums)
    mid = int(len(nums)/2)
    if len(nums) % 2 == 1:
        median = sorted_nums[mid]
    else:
        median = (sorted_nums[mid-1] + sorted_nums[mid])/2
    return median

def calc_mode(nums):
    """
    Calculates the mode of a list of numbers

    Parameters
    ----------
    nums : int
        The list of numbers for which the mode is to be calculated

    Returns
    -------
    mode : int
        The mode of the list of numbers

    """
    nums_set = sorted(set(nums))
    freq = [ nums.count(num) for num in nums_set ]
    
    max_freq = max(freq)
    max_freq_index = freq.index(max_freq)
    mode = nums_set[max_freq_index]
    return mode

def calc_iqr(nums):
    """
    Calculates the interquartile range of a list of numbers

    Parameters
    ----------
    nums : int
        The list of numbers for which the interquartile range is to be calculated

    Returns
    -------
    IQR : int
        The interquartile range of the list of numbers

    """
    sorted_nums = sorted(nums)
    half_length = int(len(nums)/2)
    first = sorted_nums[:half_length]
    
    if len(nums) % 2 == 1: #odd
        second = sorted_nums[half_length+1:]
    
    else: #even
        second = sorted_nums[half_length:]
        
    IQ1 = calc_median(first)
    IQ3 = calc_median(second)
    IQR = IQ3 - IQ1
          
    return int(IQR)

def calc_std_dev(nums):
    """
    Calculates the standard deviation of a list of numbers

    Parameters
    ----------
    nums : int
        The list of numbers for which the standard deviation is to be calculated

    Returns
    -------
    std_dev : int
        The standard deviation of the list of numbers

    """
    mean = calc_mean(nums)
    
    sqrd_devs = [ (num - mean) ** 2 for num in nums ]
    
    std_dev = sqrt(sum(sqrd_devs)/(len(nums)-1))
    
    return int(std_dev)

def calc_median_skewness(nums):
    """
    Calculates the median skewness of a list of numbers

    Parameters
    ----------
    nums : int
        The list of numbers for which the median skewness is to be calculated

    Returns
    -------
    mean_skew : float
        The median skewness of the list of numbers

    """
    mean_skew = (3*(calc_mean(nums) - calc_median(nums))) / calc_std_dev(nums)
    
    return mean_skew

def calc_correlation(x_nums, y_nums):
    """
    Calculates the correlation value between two lists of numbers

    Parameters
    ----------
    x_nums : int
        The first list of numbers
    y_nums : int
        The second list of numbers

    Returns
    -------
    cor : float
        Correlation value between the two lists of numbers

    """
    a_lst = []
    b_lst = []
    c_lst = []
    x_mean = calc_mean(x_nums)
    y_mean = calc_mean(y_nums)
    
    for (x, y) in zip(x_nums, y_nums):
        a_lst.append((x - x_mean)*(y - y_mean))
        b_lst.append((x - x_mean)**2)
        c_lst.append((y - y_mean)**2)

    cor = sum(a_lst)/( sqrt(sum(b_lst)) * sqrt(sum(c_lst)))
    
    return cor

def categoric_process(option):
    """
    Processes categorical data for ebooks/audiobooks taken out in 2020 and 
    displays data information or the selected plot

    Parameters
    ----------
    option : String
        The option selected for whether data information is to be displayed or 
        the selected plot

    Returns
    -------
    None.

    """
    ebooks = {}
    ebook_lst = []
        
    try:
        with open("library_data.csv") as lib_data:
            _ = lib_data.readline()
            
            try:
                for line in lib_data:
                    month_year, member, borrowed, returned, ebook, visit = line.split(",")                 
                    if month_year[4:6] == "20":
                        ebook = int(ebook)
                        
                        try:
                            ebook_lst.append(ebook)
                            ebooks[month_year] = ebook

                        except:
                            print("Invalid format", ebook)
            except:
                print("Error reading file") 
                
    except:
        print("Error opening file")    
    
    fig, ax = plt.subplots()
    ax.set_title("Ebooks/audiobooks taken in 2020")  
        
    if option == "p":
        try:
            for key, val in ebooks.items():
                ebooks[key] = (val/sum(ebook_lst))*100
        except:
            print("Error")
        ax.pie(ebooks.values(),labels=ebooks.keys(),autopct="%.f%%")
    
    elif option == "c":       
        y_pos = [ i for i in range(len(ebooks)) ]
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(ebooks.keys())
        
        ax.barh(y_pos, ebooks.values(), align="center")
        
    
    elif option == "b":
        ax.boxplot(ebooks.values(), showmeans = True, meanline = True)
        
    plt.show()

def histogram(dic1, dic2):
    """
    Generates histograms from dictionaries provided

    Parameters
    ----------
    dic1 : int
        Dictionary of month year keys and visit values.
    dic2 : int
        Dictionary of month year keys and items borrowed values.

    Returns
    -------
    None.

    """
    fig, axs = plt.subplots(2,1, figsize=(25, 20))
    
    axs[0].set_title("Visits to all libraries")
    axs[0].set_xlabel("Dates")
    axs[0].set_ylabel("Visits")
    axs[0].hist(dic1.values(), bins=33, ec="black")
    
    axs[1].set_title("Items borrowed from all libraries")
    axs[1].set_xlabel("Dates")
    axs[1].set_ylabel("Borrowed")
    axs[1].hist(dic2.values(), bins=33, ec="black")
    
    plt.show()
    
def boxplot(dic1, dic2):
    """
    Generates boxplot from dictionaries provided

    Parameters
    ----------
    dic1 : int
        Dictionary of month year keys and visit values.
    dic2 : int
        Dictionary of month year keys and items borrowed values.

    Returns
    -------
    None.

    """
    fig, axs = plt.subplots(1,2, figsize=(20,10))
    
    axs[0].set_title("Visits to all libraries")
    axs[0].set_ylabel("Visits")
    axs[0].boxplot(dic1, showmeans = True, meanline = True)
    
    axs[1].set_title("Items borrowed from all libraries")
    axs[1].set_ylabel("Borrowed")
    axs[1].boxplot(dic2, showmeans = True, meanline = True)
    
    plt.show()
    
def scatterplot(lst1, lst2):
    """
    Generates scatterplot from lists provided

    Parameters
    ----------
    lst1 : int
        List of visit values
    lst2 : int
        List of items borrowed values

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    
    ax.set_xlabel("Visits")
    ax.set_ylabel("Borrowed")
    
    ax.set_title("Visits vs. Borrowed")
    
    ax.scatter(lst1, lst2, marker=".")
    
    plt.show()

def numeric_process(option):
    """
    Processes numeric data for library visits and item borrowed 2019 to 2021 
    and displays data information or the selected plot

    Parameters
    ----------
    option : String
        The option selected for whether data information is to be displayed or 
        the selected plot

    Returns
    -------
    None.

    """
    visits = {}
    visit_lst = []
    visit_num = 1
        
    items_borrowed = {}
    items_borrowed_lst = []
    borrow_num = 1   
        
    try:
        with open("library_data.csv") as lib_data:
            _ = lib_data.readline()
            
            try:
                for line in lib_data:
                    month_year, member, borrowed, returned, ebook, visit = line.split(",")                  
                    visit = int(visit)
                                        
                    borrowed = int(borrowed)
                    
                    try:
                        visit_lst.append(visit)
                        while visit > 0:    
                            visits[visit_num] = month_year
                            visit -= 1
                            visit_num += 1
                                                                
                    except:
                        print("Invalid format", visit)
                    
                    #Process Borrowed Items data             
                    try:
                        items_borrowed_lst.append(borrowed)
                        while borrowed > 0:    
                            items_borrowed[borrow_num] = month_year
                            borrowed -= 1
                            borrow_num += 1
                    except:
                        print("Invalid format", borrowed)
                    
            except:
                print("Error reading file") 
     
    except:
        print("Error opening file")    
    
    #Data Info
    if option == "d":
        print("Data info")
        print("\t" * 7, "Visits", "\t", "Items Borrowed")
        print("Total number of values:", "\t", len(visit_lst), "\t" * 2, len(items_borrowed_lst))
        print("Total:", "\t" * 6, sum(visit_lst), "\t", sum(items_borrowed_lst))
        print("Mean:", "\t" * 6, int(calc_mean(visit_lst)), "\t" * 2, int(calc_mean(items_borrowed_lst)))
        print("Median:", "\t" * 5, calc_median(visit_lst), "\t" * 2, calc_median(items_borrowed_lst))
        print("Mode:", "\t" * 6, calc_mode(visit_lst), "\t" * 3, calc_mode(items_borrowed_lst))
        print("Maximum:", "\t" * 5, max(visit_lst), "\t" * 2, max(items_borrowed_lst))
        print("Minimum:", "\t" * 5, min(visit_lst), "\t" * 3, min(items_borrowed_lst))
        print("Range:", "\t" * 6, max(visit_lst)-min(visit_lst), "\t" * 2, max(items_borrowed_lst)-min(items_borrowed_lst))
        print("Inter-Quartile Range:", "\t" * 2, calc_iqr(visit_lst), "\t" * 2, calc_iqr(items_borrowed_lst))
        print("Standard Deviation:", "\t" * 2, calc_std_dev(visit_lst), "\t" * 2, calc_std_dev(items_borrowed_lst))
        print("Skewness:", "\t" * 5, f"{calc_median_skewness(visit_lst):.3f}", "\t" * 2, f"{calc_median_skewness(items_borrowed_lst):.3f}")
        print("\nCorrelation:", "\t", f"{calc_correlation(visit_lst, items_borrowed_lst):.3f}")
    
    #Histrogram
    elif option == "h":
        histogram(visits, items_borrowed)
    
    #Boxplot
    elif option == "b":
        boxplot(visits, items_borrowed)
    
    #Scatter plot
    elif option == "s":
        scatterplot(visit_lst, items_borrowed_lst)

if __name__ == "__main__":
    loop1 = True
    while loop1:
        opt1 = input("Menu 1: [N]umeric data, [C]ategorical data, [Q]uit: ")
        
        #Numeric
        if opt1.lower() == "n":
            loop2 = True
            while loop2:
                opt2 = input("\tMenu 2: [D]ata info, [P]lot options, [R]eturn: ")
                #Data Info
                if opt2.lower() == "d":
                    numeric_process("d")
            
                #Plot Options
                elif opt2.lower() == "p":
                    loop3 = True
                    while loop3:
                        opt3 = input("\t\tMenu 3: [H]istogram, [B]oxplot, [S]catter plot, [R]eturn: ")
                        #Histogram
                        if opt3.lower() == "h":
                            numeric_process("h")
                        #Boxplot
                        elif opt3.lower() == "b":
                            numeric_process("b")
                        #Scatter Plot
                        elif opt3.lower() == "s":
                            numeric_process("s")
                        #Return to opt2
                        elif opt3.lower() == "r":
                            loop3 = False
                
                #Return to opt1
                elif opt2.lower() == "r":
                    loop2 = False
                
                else:
                    print("Invalid selection")
                
        #Categorical
        elif opt1.lower() == "c":
            loop2 = True
            while loop2:
                opt2 = input("\tMenu 2: [P]lot options, [R]eturn: ")
            
                #Plot Options
                if opt2.lower() == "p":
                    loop3 = True
                    while loop3:
                        opt3 = input("\t\tMenu 3: [P]ie chart, [C]hart (barchart), [B]oxplot, [R]eturn: ")
                        #Histogram
                        if opt3.lower() == "p":
                            categoric_process("p")
                        #Boxplot
                        elif opt3.lower() == "c":
                            categoric_process("c")
                        #Scatter Plot
                        elif opt3.lower() == "b":
                            categoric_process("b")
                        #Return to opt2
                        elif opt3.lower() == "r":
                            loop3 = False
                
                #Return to opt1
                elif opt2.lower() == "r":
                    loop2 = False
        
                else:
                    print("Invalid selection")
        
        #Quit        
        elif opt1.lower() == "q":
            loop1 = False
            
        else:
            print("Invalid selection")