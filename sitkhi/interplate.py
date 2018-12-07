import SimpleITK as sitk


def respacing(itk_img, save_name, new_spacing):
    """given newspacing, resample the src image.
    
    Args:
        itk_img: Sitk image i.e. ITK image Object.
        save_name: Resampled image save name.
        new_spacing: The new spacing.
        
    Returns:
        None
    """
    spacing = itk_img.GetSpacing()
    size = itk_img.GetSize()
    new_size = [int(ori_size*ori_spa/new_spa) for ori_size, ori_spa, new_spa in zip(size, spacing, new_spacing)]
    reference_image = sitk.Image(new_size, itk_img.GetPixelIDValue())
    reference_image.SetOrigin(itk_img.GetOrigin())
    reference_image.SetDirection(itk_img.GetDirection())
    reference_image.SetSpacing(new_spacing)
    resample = sitk.Resample(itk_img, reference_image)
    writer = sitk.ImageFileWriter()
    writer.SetFileName(save_name)
    writer.Execute(resample)
    
def resize(itk_img, save_name, new_size):
    """Resize image to [new_size, new_size, ?] in a  Equal Proportion.
    
    Args: 
        itk_img: Sitk image i.e. ITK image Object.
        save_name: Resampled image save name.
        new_size: new size.
        
    Returns:
        None
    """
    print("original spacing:", itk_img.GetSpacing())
    print(itk_img.GetSize())
    factor = new_size / (itk_img.GetSize()[0])
    new_size = [new_size, new_size, itk_img.GetSize()[2] // 2]
    reference_image = sitk.Image(new_size, itk_img.GetPixelIDValue())
    reference_image.SetOrigin(itk_img.GetOrigin())
    reference_image.SetDirection(itk_img.GetDirection())
    reference_image.SetSpacing([sz*spc/nsz for nsz,sz,spc in zip(new_size, itk_img.GetSize(), itk_img.GetSpacing())])
    s1 = sitk.Resample(itk_img, reference_image)
    print("resize spacing:", s1.GetSpacing())
    print("resize", s1.GetSize(), '\n')
    writer = sitk.ImageFileWriter()
    writer.SetFileName(save_name)
    writer.Execute(s1)
