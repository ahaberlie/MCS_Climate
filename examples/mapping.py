import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
import numpy as np
import copy
import string
letters = string.ascii_lowercase

projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=37.5, standard_parallels=(29.5, 45.5))

conus_extents = {'ECONUS': [-110, -73.5, 22, 49]}
longitutde_display = {'ECONUS': [-110, -100, -90, -80, -70]}

def get_color_dict(figure):

    if figure == 1:

        raw_values = [1, 5, 10, 20, 30, 40, 50]
        diff_values = [-15, -10, -5, -1, 1, 5, 10, 15]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 2:

        raw_values = [1, 2, 3, 5, 10, 15, 20]
        diff_values = [-7, -5, -3, -1, 1, 3, 5, 7]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 6:

        raw_values = [1, 2, 3, 4, 5, 6, 7]
        diff_values = [-3, -2, -1, -0.001, 0.001, 1, 2, 3]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 7:

        raw_values = [1, 100, 200, 300, 400, 500, 600]
        diff_values = [-250, -150, -50, -1, 1, 50, 150, 250]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 8:

        raw_values = [1, 25, 50, 100, 150, 200, 250]
        diff_values = [-150, -100, -50, -1, 1, 50, 100, 150]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 11:

        raw_values = [1, 3, 5, 7, 9, 11, 13]
        diff_values = [-4, -3, -2, -1, 1, 2, 3, 4]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 'S5':

        raw_values = [1, 25, 50, 100, 150, 200, 250]
        diff_values = [-100, -50, -25, -10, 10, 25, 50, 100]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    elif figure == 'S6':

        raw_values = [1, 3, 6, 9, 12, 15, 18]
        diff_values = [-7, -5, -3, -1, 1, 3, 5, 7]
        
        raw_colors = ['#ffffcc','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8']
        diff_colors = ['#bf812d','#dfc27d','#f6e8c3','#f5f5f5','#c7eae5','#80cdc1','#35978f']
        
        raw_over = '#0c2c84'
        diff_over = '#01665e'
        
        raw_under = 'grey'
        diff_under = '#8c510a'

    else:
        raise ValueError("Colormap not defined", figure)
        
    cmap = colors.ListedColormap(raw_colors)
    cmap.set_over(raw_over)
    cmap.set_under(raw_under)
    norm = colors.BoundaryNorm(raw_values, ncolors=cmap.N)
    
    dcmap = colors.ListedColormap(diff_colors)
    dcmap.set_over(diff_over)
    dcmap.set_under(diff_under)
    dnorm = colors.BoundaryNorm(diff_values, ncolors=dcmap.N)
        
    colori = {'historical': {'cmap': cmap, 'norm': norm},
               'future_4p5': {'cmap': cmap, 'norm': norm},
               'future_8p5': {'cmap': cmap, 'norm': norm},
               'delta_future_4p5': {'cmap': dcmap, 'norm': dnorm},
               'delta_future_8p5': {'cmap': dcmap, 'norm': dnorm}}

    return colori

def draw_geography(ax):
        
    countries_shp = shpreader.natural_earth(resolution='50m',
                                     category='cultural',
                                     name='admin_0_countries')
    
    for country, info in zip(shpreader.Reader(countries_shp).geometries(), 
                             shpreader.Reader(countries_shp).records()):
        if info.attributes['NAME_LONG'] != 'United States':

            ax.add_geometries([country], ccrs.PlateCarree(),
                             facecolor='Grey', edgecolor='k', zorder=6)
            
    lakes_shp = shpreader.natural_earth(resolution='50m',
                                     category='physical',
                                     name='lakes')
    
    for lake, info in zip(shpreader.Reader(lakes_shp).geometries(), 
                             shpreader.Reader(lakes_shp).records()):

        name = info.attributes['name']
        if name == 'Lake Superior' or name == 'Lake Michigan' or \
           name == 'Lake Huron' or name == 'Lake Erie' or name == 'Lake Ontario':
            
            ax.add_geometries([lake], ccrs.PlateCarree(),
                              facecolor='lightsteelblue', edgecolor='k', zorder=6)
            
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'ocean', '50m', edgecolor='face', 
                                                facecolor='lightsteelblue'), zorder=6)

    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'coastline', '50m', edgecolor='face', 
                                                facecolor='None'), zorder=6) 
    
    shapename = 'admin_1_states_provinces_lakes'
    states_shp = shpreader.natural_earth(resolution='50m',
                                     category='cultural', name=shapename)
                                     
    for state, info in zip(shpreader.Reader(states_shp).geometries(), shpreader.Reader(states_shp).records()):
        if info.attributes['admin'] == 'United States of America':

            ax.add_geometries([state], ccrs.PlateCarree(),
                              facecolor='grey', edgecolor='k')
            
    for state, info in zip(shpreader.Reader(states_shp).geometries(), shpreader.Reader(states_shp).records()):
        if info.attributes['admin'] == 'United States of America':

            ax.add_geometries([state], ccrs.PlateCarree(),
                              facecolor='None', edgecolor='k', zorder=6)

def draw_region_outlines(ax):
    
    usa = gpd.read_file("../data/geog/CONUS.shp")
    
    quadrants = {'NP': {'states': ['NE', 'SD', 'ND'], 
                    'ax_label': 'i.'},
                 'SP': {'states': ['TX', 'OK', 'KS'], 
                        'ax_label': 'ii.'},
                 'MW': {'states': ['WI', 'MI', 'OH', 
                                   'IL', 'IN', 'MN', 
                                   'IA', 'MO', 'KY'], 
                        'ax_label': 'iii.'},
                 'SE': {'states': ['AR', 'LA', 'TN', 
                                   'MS', 'AL', 'SC', 
                                   'NC', 'FL', 'GA'], 
                        'ax_label': 'iv.'},
                 'NE': {'states': ['NJ', 'PA', 'NY', 
                                   'VT', 'NH', 'CT', 
                                   'VA', 'WV', 'MD', 
                                   'DC', 'DE', 'RI', 
                                   'MA', 'ME'], 
                        'ax_label': 'v.'}}

    for qid, quad_info in quadrants.items():

        usa_dis = usa[usa.STUSPS.isin(quad_info['states'])]
        usa_dis = copy.deepcopy(usa_dis.dissolve())

        ctr = usa_dis.to_crs('ESRI:102004').centroid.to_crs('EPSG:4269')

        ax.add_geometries(usa_dis.geometry.values, crs=ccrs.PlateCarree(), 
                          linewidths=5, facecolor='None', zorder=15)

        ax.text(ctr.x.values[0]-2.5, ctr.y.values[0], quad_info['ax_label'], 
                transform=ccrs.PlateCarree(), fontsize=25, zorder=15)

def spec_ax(position, fig, nrows, ncols=None, colpos=None, five_panel=False):

    gs0 = gridspec.GridSpec(nrows, 1, figure=fig)
    gs0.update(wspace=0.25, hspace=0.25)

    if five_panel:
        if position == 0:
            cur_gs = gs0[position].subgridspec(2, 4)   
            ax = fig.add_subplot(cur_gs[:, 1:3], projection=projection)
        else:
            cur_gs = gs0[int(np.ceil(position/2))].subgridspec(2, 2)
            ax = fig.add_subplot(cur_gs[:, 1-(position%2)], projection=projection)

    else:
        cur_gs = gs0[position].subgridspec(1, ncols)

        ax = fig.add_subplot(cur_gs[:, colpos], projection=projection)

    return ax

def setup_map(label_num, ax=None, num=None, rows=None, cols=None, 
              draw_outlines=False, extent='ECONUS', longitudes='ECONUS'):
    
    if ax is None:
        ax = plt.subplot(rows, cols, num, projection=projection)

    ax.set_extent(conus_extents[extent])

    draw_geography(ax)

    if draw_outlines and label_num==1:
        draw_region_outlines(ax)

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, dms=True, x_inline=False, y_inline=False, zorder=10,
                      color='k', alpha=0.5)

    gl.top_labels = False

    gl.right_labels = False

    gl.xlocator = mticker.FixedLocator(longitutde_display[longitudes])

    gl.xlabel_style = {'size': 20, 'color': 'k', 'rotation': 0.01}
    gl.ylabel_style = {'size': 20, 'color': 'k'}
    
    ax.annotate("{})".format(letters[label_num-1]), (-.06,1), xycoords='axes fraction',
                fontsize=26, bbox=dict(boxstyle='round', facecolor='w', alpha=1), 
                color='k', zorder=25)

    return ax