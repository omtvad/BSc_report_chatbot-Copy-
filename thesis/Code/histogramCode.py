import matplotlib.pyplot as plt
import matplotlib

def get_histogram(df, shape=(3, 3), bins=10, super_title=None,
                  super_title_size=10, title_size=6, alpha=0.5, figsize=(8.27, 11.69)):
					
    matplotlib.style.use('ggplot')    # Changes the plot style
    subfigs_per_fig = (shape[0] * shape[1])    # Calculates to number of subfigs per fig
    columns = len(df.columns)    # Finds total number of features
    matplotlib.rcParams.update({'font.size': title_size})    # Set user-spesified title size
    
    # Checks whether to create one of more figures
    if columns > subfigs_per_fig:
        figs = round(0.5 + columns / subfigs_per_fig)    # Calculates needed fig count
	
	# Iterate through figs and input histograms
        for i in range(0, figs):
            df[df.columns[0 + subfigs_per_fig * i:subfigs_per_fig * (i + 1)]].plot(kind='hist',
                subplots=True, layout=shape,  alpha=alpha, figsize=figsize) # Plot histograms

            matplotlib.rcParams.update({'font.size': super_title_size}) # Set super title size 
            plt.suptitle(super_title)    # Set super title
            matplotlib.rcParams.update({'font.size': title_size}) # Reset font size
    else:
        df.plot(kind='hist', subplots=True, layout=shape, alpha=alpha, figsize=figsize)
        matplotlib.rcParams.update({'font.size': super_title_size})
        plt.suptitle(super_title)
    
    # Show figures
    plt.show()