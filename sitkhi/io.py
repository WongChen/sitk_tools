import SimpleITK as sitk


def save_sitk(itk_img, nda, save_name):
    """convert nda to itk image with the meta info given by itk_img
    
    Args:
        itk_img: Sitk Image object.
        nda: Modified image nd array.
    """
    image = sitk.GetImageFromArray(nda)
    image.SetSpacing(itk_img.GetSpacing())
    image.SetOrigin(itk_img.GetOrigin())
    image.SetDirection(itk_img.GetDirection())
    writer = sitk.ImageFileWriter()
    writer.SetFileName(save_name)
    writer.Execute(image)
