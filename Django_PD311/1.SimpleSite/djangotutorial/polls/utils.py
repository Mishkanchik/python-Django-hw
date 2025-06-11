from uuid import UUID
from PIL import Image
import io
from django.core.files.base import ContentFile
import uuid

def optimize_image(image_field, max_size=(800, 800), quality=85):
    
    if not image_field:
        return None

   
    img = Image.open(image_field).convert('RGB')


    img = img.resize(max_size, Image.Resampling.LANCZOS)


    output = io.BytesIO()
    img.save(output, format='WEBP', quality=quality, optimize=True)
    output.seek(0)


    optimized_image = ContentFile(output.getvalue())
    
  
    uid=str(uuid.uuid4())[:8] 

    new_name = f"{uid}.webp"
    
    return optimized_image, new_name 