from matplotlib import pyplot as plt
from ipywidgets import interact, fixed

def show_slices(slices, title=None):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")
        if title is not None:
            axes[i].set_title(title)

def display3(direction, slices):
    '''display 3d images interactively
    Args:
        direction: axial, sagittal or coronal, str.
        slices: List of 3d numpy arrays.

    '''
    if direction.lower() not in ['axial', 'sagittal', 'coronal']:
        raise ValueError('direction must be one of {}'.format('axial, sagittal, coronal'))
    direction = direction.lower()
    mm = {'axial': 0, 'sagittal': 1, 'coronal': 2}
    dire_num = mm.get(direction)
    ms = slices[0].shape[dire_num]
    for s in slices:
        if len(s.shape) != 3:
            raise ValueError('input volume array must be 3 dimentional')
        if s.shape[dire_num] != ms:
            raise ValueError('input volume arrays must have same length in {} direction'.format(direction))
    def callback(i):
        '''call back for the interact func'''
        if direction == 'axial':
            new_slices = [img[i, :, :] for img in slices]
        if direction == 'sagittal':
            new_slices = [img[:, i, :] for img in slices]
        if direction == 'coronal':
            new_slices = [img[:, :, i] for img in slices]
        show_slices(new_slices)
    interact(callback, i=(0, ms-1))
