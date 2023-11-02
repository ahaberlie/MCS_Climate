import requests
import os
from bs4 import BeautifulSoup

def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

def download_geography(data_dir="../data", print_urls=False, create_dirs=True, verbose=False):

    geo_dir = f"{data_dir}/geog"
    if create_dirs:
        if not os.path.exists(geo_dir):
           os.makedirs(geo_dir)

    for ext in ['.cpg', '.dbf', '.prj', '.sbn', '.sbx', '.shp', '.xml', '.shx']:

        url = "https://svrimg.niu.edu/npjcas23/"

        result = get_url_paths(url, ext)

        for url in result:

            if print_urls:
                print(url)
            else:
                fname = url.replace("%20", " ")
    
                fname = fname.split("/")[-1]

                fname = f"{geo_dir}/{fname}"
    
                if not os.path.exists(fname):
    
                    r = requests.get(url)
                    with open(fname, 'wb') as f:
                        f.write(r.content)

                    if verbose:
                        print("Downloaded", fname)
                else:
                    if verbose:
                        print(fname, "exists")
    
    
def download(analysis, subset, data_dir="../data", verbose=False, create_dirs=False,
             print_urls=False):
    '''
    Takes an analysis and subset to download.

    You must explicitly change 'create_dirs' to allow
    creation of directories automatically. If you do not,
    make sure you manually create the correct directories.

    It is easier to do it automatically, but I don't want to 
    force this option on anyone.

    You can also use print_urls to manually download the netcdf files

    analysis options:

    mcs_days
    mcs_precipitation
    mcs_attributes

    subset options

    historical_monthly
    future_4p5_monthly
    future_8p5_monthly
    '''

    outdir = f"{data_dir}/{analysis}/{subset}"

    if create_dirs:
        if not os.path.exists(outdir):
            os.makedirs(outdir)
    
    for ext in ['.nc']:

        url = f"https://svrimg.niu.edu/climc23/{analysis}/{subset}/"

        result = get_url_paths(url, ext)

        for url in result:

            if print_urls:

                print(url)

            else:

                fname = url.replace("%20", " ")
    
                fname = fname.split("/")[-1]
    
                fname = f"{outdir}/{fname}"
                
                if not os.path.exists(fname):
    
                    r = requests.get(url)
                    with open(fname, 'wb') as f:
                        f.write(r.content)
    
                    if verbose:
                        print("Downloaded", fname)
                else:
                    if verbose:
                        print(fname, "exists")