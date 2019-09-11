from __future__ import print_function
import os
import csv
from pySmartDL import SmartDL
from pySmartDL.utils import get_filesize
from shapely.geometry import shape, mapping
import fiona

def demdownload(infile=None,destination=None):
    with fiona.open(infile) as input:
        for pol in input:
            reader= pol['properties']['fileurl']
            fname= os.path.basename(reader)
            fpath=os.path.join(destination,fname)
            if not os.path.exists(fpath):
                url=reader
                dest=destination
                print(url)
                fsize = get_filesize(url)
                if fsize < 21e6:
                    nthread = 1
                elif fsize < 42e6:
                    nthread = 2
                elif fsize < 100e6:
                    nthread = 3
                elif fsize < 200e6:
                    nthread = 4
                elif fsize < 400e6:
                    nthread = 5
                else:
                    nthread = 6
                obj=SmartDL(url,dest, threads=nthread)
                obj.start()
                path=obj.get_dest()
            else:
                print('Skipping....' + str(fname))
                # print("Skipping...."+str(fname), end='\r')
        print("Download Completed")
            
