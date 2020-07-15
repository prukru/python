import datetime
import urllib2
from datetime import timedelta
import os
import subprocess

#end date of download is today
today = datetime.date.today()
end_dt=today.strftime("%m-%d-%Y")

#Start date of download is hardcoded to Jan 21
start_dt = datetime.date(2020, 1, 21)
strt_dt= start_dt.strftime("%m-%d-%Y")

#increment download by 1 day while downloading files
test=str(strt_dt)
delta = timedelta(days=1)

#have common prefix and suffix of link in variables
common_prefix="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
common_suffix=".csv"

#convert strt_dt_obj to datetime
strt_dt_obj=datetime.datetime.strptime(strt_dt, '%m-%d-%Y')
#convert end_dt to datetime
end_dt=datetime.datetime.strptime(end_dt, '%m-%d-%Y')
end_dt = end_dt - delta

#mkdir
if not os.path.exists('data'):
    os.makedirs('data')

covdir = os.path.join('data','covid19')

if not os.path.exists(covdir):
    os.makedirs(covdir)

#Base directory
_dir = "data/covid19"

while strt_dt_obj < end_dt:

        strt_dt_obj += delta
        strt_dt=strt_dt_obj.strftime("%m-%d-%Y")

        #Getdate for creating folder
        strt_obj_path= strt_dt[:2]+strt_dt[3:5]+strt_dt[6:10]

        #create dynamic name for subfolder everyday
        _dirsub = os.path.join(_dir,strt_obj_path)
        if not os.path.exists(_dirsub):
                os.makedirs(_dirsub)

                #complete url
                comp_url_link = common_prefix+strt_dt+common_suffix
                print("From Source file path", comp_url_link)

                #FIlePath with FIle Name
                filename = strt_dt + common_suffix
                filepath = os.path.join(_dirsub,filename)
                print("Local Destination file path", filepath)

                #Download csv from the url link
                filedata = urllib2.urlopen(comp_url_link)
                datatowrite = filedata.read()
                with open(filepath,'wb') as f:
                        f.write(datatowrite)



        #convert strt_dt_obj to datetime
        strt_dt_obj=datetime.datetime.strptime(strt_dt, '%m-%d-%Y')

else:

        print("All files already downloaded and copied to Local. COpying files to hdfs now.")

        #Remove backups from hdfs before copying files to hdfs
        subprocess.call(['hadoop fs -rm -r /data/covid19/'],shell=True)


        #create covid directory in hdfs inside/data folder
        subprocess.call(['hadoop fs -mkdir /data/covid19'],shell=True)

        #Copy from Local to Hadoop
        #subprocess.call(['hadoop fs -put /home/cloudera/Desktop/data/covid19  /data/'],shell=True)
        DEVNULL = open(os.devnull, 'wb')
        ps = subprocess.Popen(['hadoop fs -put /home/cloudera/Desktop/data/covid19  /data/'],shell=True,stdout=DEVNULL,stderr=DEVNULL)


        print("All data files downloaded local and uploaded in hdfs successfully.")

        raise SystemExit()
