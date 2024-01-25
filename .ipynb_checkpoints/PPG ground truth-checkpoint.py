def ground_truth():
    Channel_two = [3,6,7,11,12,15,18,22,27,30,34,36,43]
    Channel_five = [1,2,5,8,9,10,19,20,37,42,44,50,51]
    for idx in range(1,54):
        data = r"bidmc-ppg-and-respiration-dataset-1.0.0\bidmc_csv\bidmc_"+str(idx).zfill(2)+r"_Signals.csv"
        data = pd.read_csv(data)
        cols = data.columns
        if idx in Channel_two or idx in Channel_five:
            PPG = np.array(data[' PLETH'].to_list())
            if idx in Channel_two:
                ECG = np.array(data[" II"].to_list())
            else:
                ECG = np.array(data[" V"].to_list())
            xqrs = processing.XQRS(sig=np.array(ECG), fs=125)
            xqrs.detect()
            gt_peaks = [xqrs.qrs_inds]
            plt.figure(figsize=(12, 2))
            plt.plot(PPG)
            plt.scatter(gt_peaks, PPG[gt_peaks], c = "red", s = 8)
            plt.xlim((0,5000))
            plt.show()