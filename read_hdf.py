import h5py

with h5py.File('burnt_area_clipped_nd.h5', 'r') as hdf:
    print(list(hdf.keys()))
    for a in hdf:
        print(a)
        rp = hdf[a]

        
        for key in rp.keys():
            #print(list(hdf[a].get(key)))
            print(key)
            #print(rp[key].shape)
            #print(rp.get(key))
            #print(rp[key][()])
        

