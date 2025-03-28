import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('zigzag.png')
image_arr = np.array(img)

plt.imshow(image_arr)
print(image_arr.shape)
plt.show()

"""

1. Selection & Masking (Finding Pixels in the Interval)
Finding Pixels Within a Certain Range
np.where(condition[, x, y])

condition → A Boolean array defining which pixels to modify.

x (optional) → Value to place where the condition is True.

y (optional) → Value to place where the condition is False.

Example use case: np.where((image[:,:,0] > 100) & (image[:,:,0] < 200))

np.logical_and(x1, x2, /, *[, out, where])

x1 & x2 → Boolean conditions to be combined with AND logic.

Example: np.logical_and(image[:,:,0] > 100, image[:,:,0] < 200)

np.logical_or(x1, x2, /, *[, out, where])

x1 & x2 → Boolean conditions to be combined with OR logic.

Example: np.logical_or(image[:,:,0] < 50, image[:,:,2] > 200)

np.logical_not(x, /, *[, out, where])

x → Boolean array to negate.

Example: np.logical_not(mask) (inverts the mask).

np.all(a, axis=None, keepdims=False, *, where=True)

a → The input array (e.g., image_array).

axis=2 → Checks if all conditions are True for RGB channels.

Example: np.all((image > 100) & (image < 200), axis=2)

np.any(a, axis=None, keepdims=False, *, where=True)

a → The input array.

axis=2 → Checks if any condition is True for RGB channels.

Example: np.any(image > 200, axis=2) # Detects if any RGB value is > 200

2. Array Indexing & Modification (Changing RGB Values)
Boolean Indexing

image_array[mask] = new_value

Example: image_array[(image_array[:,:,0] > 100) & (image_array[:,:,0] < 200)] = [255, 0, 0] (turns selected pixels red).

Array Slicing

image_array[:, :, 0] → Modify Red channel.

image_array[:, :, 1] → Modify Green channel.

image_array[:, :, 2] → Modify Blue channel.

Example: image_array[:, :, 0] += 50 (increases red intensity).

3. Clamping & Normalization (Ensuring Valid RGB Values)
np.clip(a, a_min, a_max, out=None, *, where=True)

a → The input array.

a_min → Minimum value (0 for RGB).

a_max → Maximum value (255 for RGB).

Example: np.clip(image_array, 0, 255) (ensures valid RGB values).

array.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)

dtype → Target data type (np.uint8 for images).

Example: image_array.astype(np.uint8) (ensures correct image format).

4. Arithmetic Operations (For Transforming RGB Values)
np.add(x1, x2, /, out=None, *, where=True, dtype=None, casting='same_kind')

x1 & x2 → Arrays to add.

Example: np.add(image_array, 50) (increases brightness).

np.subtract(x1, x2, /, out=None, *, where=True, dtype=None, casting='same_kind')

x1 & x2 → Arrays to subtract.

Example: np.subtract(image_array, 30) (darkens image).

np.multiply(x1, x2, /, out=None, *, where=True, dtype=None, casting='same_kind')

x1 & x2 → Arrays to multiply.

Example: np.multiply(image_array, 1.2) (increases contrast).

np.divide(x1, x2, /, out=None, *, where=True, dtype=None, casting='same_kind')

x1 & x2 → Arrays to divide.

Example: np.divide(image_array, 2) (reduces brightness by half).

np.dot(a, b, out=None)

a → Input array (e.g., image_array).

b → Matrix for transformation.

Example: np.dot(image_array, [[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1.2]]) (modifies RGB intensity).

5. Copying & Structuring Data (Avoiding In-Place Modification Issues)
np.copy(a, order='K')

a → The array to copy.

Example: copy_img = np.copy(image_array) (avoids modifying the original image).

np.zeros_like(a, dtype=None, order='K', subok=True, shape=None)

a → The reference array.

Example: new_img = np.zeros_like(image_array) (creates an empty image).

np.ones_like(a, dtype=None, order='K', subok=True, shape=None)

a → The reference array.

Example: new_img = np.ones_like(image_array) * 255 (creates a white image).

"""