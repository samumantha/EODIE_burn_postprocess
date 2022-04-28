import h5py
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib as mpl
from scipy import interpolate


burndates= {
'130': '20210701',
'2854': '20210607',
'269': '20210617',
'190': '20210706',
'214': '20210630'}

# tls dates
prepostdates= {
    '130' : ['20210618','20210904'],
    '2854' : ['20210604','20210628'],
    '269' : ['20210614','20210903'],
    '190' : ['20210608','20210907'],
    '214': ['20210611', '20210906']
}

#from get_closest(below)
preposts2tlsdates = {'130': ['20210617', '20210909'], '2854': ['20210604', '20210701'], '269': ['20210611', '20210902'], '190': ['20210608', '20210906'], '214': ['20210611', '20210828']}

def get_closest(prepostdates, keydatedict):
    closesttlsdict = {}
    for id in prepostdates.keys():
        predatestring = prepostdates[id][0]
        postdatestring = prepostdates[id][1]
        predate = datetime.datetime.strptime(predatestring,"%Y%m%d").date()
        postdate = datetime.datetime.strptime(postdatestring,"%Y%m%d").date()
        avdates = keydatedict[id]
        #print(avdates)
        precurdelta = 100
        postcurdelta = 100
        for avdate in avdates:
            avdate = datetime.datetime.strptime(avdate,"%Y%m%d").date()
            
            #print(avdate)
            predelta = predate - avdate
            predeltadays = predelta.days
            # if pre burndate
            predeltadays = np.abs(predeltadays)

            #print(predate)
            #print(avdate)
            #print(predeltadays) 
                 
            if predeltadays < precurdelta:                       
                precurdelta = predeltadays
                predatetormember = avdate
                
                
            
            #print(avdate)
            postdelta = postdate - avdate
            postdeltadays = postdelta.days
            # if post burndate
            postdeltadays = np.abs(postdeltadays)

            #print(postdate)
            #print(avdate)
            #print(postdeltadays) 
            
            if postdeltadays < postcurdelta:
                postcurdelta = postdeltadays
                postdatetoremeber = avdate
                

        if not id in closesttlsdict.keys():
            closesttlsdict[id] = [predatetormember.strftime('%Y%m%d')]
            closesttlsdict[id].append(postdatetoremeber.strftime('%Y%m%d'))




        print('closest')
        print(id)
        print(precurdelta)
        print(predate)
        print(postcurdelta)
        print(postdate)
    print(closesttlsdict)

#only non cloudy dates
keydatedict = {'130': ['20210512', '20210513', '20210518', '20210520', '20210523', '20210528', '20210530', '20210601', '20210602', '20210604', '20210606', '20210607', '20210609', '20210611', '20210617', '20210621', '20210627', '20210629', '20210701', '20210702', '20210704', '20210707', '20210712', '20210714', '20210716', '20210717', '20210726', '20210806', '20210810', '20210813', '20210821', '20210909', '20210927', '20211014', '20211019'], '190': ['20210512', '20210517', '20210519', '20210601', '20210606', '20210608', '20210611', '20210613', '20210623', '20210626', '20210703', '20210706', '20210716', '20210726', '20210802', '20210807', '20210815', '20210906', '20211004', '20211019', '20211024'], '214': ['20210512', '20210525', '20210530', '20210604', '20210606', '20210609', '20210611', '20210619', '20210626', '20210629', '20210704', '20210714', '20210716', '20210726', '20210813', '20210828', '20210927', '20211019', '20211029'], '269': ['20210204', '20210206', '20210209', '20210211', '20210214', '20210326', '20210331', '20210412', '20210415', '20210417', '20210430', '20210512', '20210527', '20210530', '20210606', '20210611', '20210619', '20210621', '20210626', '20210701', '20210704', '20210714', '20210716', '20210724', '20210726', '20210810', '20210813', '20210902', '20210927', '20211017', '20211019'], '2854': ['20210512', '20210524', '20210529', '20210530', '20210604', '20210611', '20210616', '20210618', '20210619', '20210621', '20210701', '20210703', '20210704', '20210711', '20210714', '20210716', '20210718', '20210721', '20210726', '20210731', '20210808', '20210810', '20210813', '20210902', '20210904', '20210916', '20210926', '20211006', '20211024']}

get_closest(prepostdates,keydatedict)

names = {
    '130': 'Seitseminen',
    '2854': 'Nuuksio',
    '269':'Liesjarvi',
    '190':'Kivimaensalo/Ahveninen',
    '214': 'Pyha-Hakki'
}

preposts2dates = {
'130': ['20210629','20210702'],
'2854': ['20210604','20210611'],
'269': ['20210611','20210619'],
'190': ['20210703','20210716'],
'214': ['20210629','20210704']
}


with h5py.File('burnt_area_clipped_nd_fixed.h5', 'r') as hdf:
    print(list(hdf.keys()))
    for a in hdf:
        print(a)
        rp = hdf[a]



        oneidmedians = {}
        oneidnotallpixels = {}
        preburn = []
        postburn = []
        #print(rp.keys())

        for key in rp.keys():
            #print(list(hdf[a].get(key)))
            #print(key)

            
            #print(rp[key].shape)
            #print(rp.get(key))
            #real values are between -1 and 1
            if not int(key) in oneidmedians.keys():
                df = rp[key][()]
                 
                #print(np.count_nonzero(df[df==99999]))
                if np.count_nonzero(df[df==99999]) == 0: 
                    
                    #print(preposts2dates)
                    preTLS = rp[preposts2tlsdates[a][0]]
                    postTLS = rp[preposts2tlsdates[a][1]]

                    pres2 = rp[preposts2dates[a][0]]
                    posts2 = rp[preposts2dates[a][1]]

                    dnbrtls = np.subtract(preTLS,postTLS)
                    dnbrs2 = np.subtract(pres2,posts2)

                    rdnbrtls = np.divide(dnbrtls,np.sqrt(np.abs(preTLS)))
                    rdnbrs2 = np.divide(dnbrs2,np.sqrt(np.abs(pres2)))

                    df[(df < -1) | (df > 1)] = np.nan
                    datekey = datetime.datetime.strptime(key,"%Y%m%d").date() 
                    datekey2 = mpl.dates.date2num(datekey)
                    median = np.nanmedian(df)
                    
                    if datekey > datetime.datetime.strptime('20210501',"%Y%m%d").date() and datekey < datetime.datetime.strptime(burndates[a],"%Y%m%d").date():
                        preburn.append(median)
                    elif datekey > datetime.datetime.strptime(burndates[a],"%Y%m%d").date() and datekey < datetime.datetime.strptime('20210930',"%Y%m%d").date():
                        postburn.append(median)
                    oneidmedians[datekey] = median
                else : 
                    df[(df < -1) | (df > 1)] = np.nan
                    datekey = datetime.datetime.strptime(key,"%Y%m%d").date() 
                    datekey2 = mpl.dates.date2num(datekey)
                    median = np.nanmedian(df)
                    oneidnotallpixels[datekey] = median
        """
        #print(dnbrs2)
        #print(dnbrtls)
        #print(rdnbrs2)
        #print(rdnbrtls)
        plt.imshow(dnbrs2)
        plt.colorbar()
        plt.clim(0, 0.6) 
        plt.title('dnbr s2 ' + names[a] + ' - '+ a)
        plt.savefig('dnbr_s2_id_'+ a+ '.png')
        plt.show()
        plt.clf()
        plt.imshow(dnbrtls)
        plt.colorbar()
        plt.clim(0, 0.6) 
        plt.title('dnbr tls ' + names[a] + ' - '+ a)
        plt.savefig('dnbr_tls_id_'+ a+ '.png')
        plt.show()
        plt.clf()
        plt.imshow(rdnbrs2)
        plt.colorbar()
        plt.clim(0, 0.6) 
        plt.title('rdnbr s2 ' + names[a] + ' - '+ a)
        plt.savefig('rdnbr_s2_id_'+ a+ '.png')
        plt.show()
        plt.clf()
        plt.imshow(rdnbrtls)
        plt.colorbar()
        plt.clim(0, 0.6) 
        plt.title('rdnbr tls ' + names[a] + ' - '+ a)
        plt.savefig('rdnbr_tls_id_'+ a+ '.png')
        plt.show()
        plt.clf()
        """

        #print(oneidmedians)

        preburnmedian = np.nanmedian(np.array(preburn))
        postburnmedian = np.nanmedian(np.array(postburn))


        print(np.median(dnbrs2))
        print(np.median(rdnbrs2))
        #print(preburnmedian)
        #print(postburnmedian)
        #dnbr = np.subtract(preburnmedian,postburnmedian)
        #print(dnbr)
        #print((dnbr/np.sqrt(np.abs(preburnmedian))))
        """
        #print(*sorted(oneidmedians.items()))
        #print(*sorted(oneidmedians.items()))
        plt.plot(*zip(*sorted(oneidmedians.items())), 'om', label= 'median NBR')
        plt.plot(*zip(*sorted(oneidnotallpixels.items())), 'ok', label= 'median NBR, cloudcovered')

        #x_new = np.linspace(18748, 18885, 300)

        #a_BSpline = interpolate.make_interp_spline(*zip(*sorted(oneidmedians.items())),check_finite=False)

        #y_new = a_BSpline(x_new)
        #plt.plot(x_new, y_new)
        #plt.plot(, dict(*zip(*sorted(oneidmedians.items()))).items(), '*g')
        #(k, v) for k, v in zip(keys, values)
        plt.title(names[a] + ' - ' + a)
        plt.axvline(x=datetime.datetime.strptime(burndates[a],"%Y%m%d").date() , color='tab:orange', label = 'burndate')
        plt.axvline(x=datetime.datetime.strptime(prepostdates[a][0],"%Y%m%d").date() , color='tab:purple', linestyle = '--', label= 'pre-burn TLS')
        plt.axvline(x=datetime.datetime.strptime(prepostdates[a][1],"%Y%m%d").date() , color='tab:purple', linestyle= '--', label= 'post-burn TLS')
        
        burnnumber = mpl.dates.date2num(datetime.datetime.strptime(burndates[a],"%Y%m%d").date())
        plt.axhline(y= preburnmedian, color = 'tab:blue', label= 'pre-burn median', linestyle= 'dotted')
        plt.axhline(y= postburnmedian, color= 'tab:olive', label = 'post-burn median', linestyle = 'dotted')
        plt.gca().set_xbound(datetime.date(2021, 5, 1), datetime.date(2021, 9, 30))
        plt.gca().set_ybound(-0.2,1)
        #locs, labels = plt.xticks()
        #print(locs)
        
        print(burnnumber)
        plt.xticks(rotation = 90)
        plt.ylabel('NBR')
        plt.tight_layout()
        plt.legend()

        plt.savefig("timeseries_id" + a + '.png')
        plt.show()
        plt.clf()
        """



"""
closest
130
1
2021-06-18
5
2021-09-04
closest
2854
0
2021-06-04
3
2021-06-28
closest
269
3
2021-06-14
1
2021-09-03
closest
190
0
2021-06-08
1
2021-09-07
closest
214
0
2021-06-11
9
2021-09-06
"""