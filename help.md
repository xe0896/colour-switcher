# NumPy Image Processing

## 1. Selection & Masking (Finding Pixels in the Interval)

### Finding Pixels Within a Certain Range

#### `np.where(condition[, x, y])`
- `condition` → Boolean array defining which pixels to modify
- `x` (optional) → Value where condition is True  
- `y` (optional) → Value where condition is False  
Example: `np.where((image[:,:,0] > 100) & (image[:,:,0] < 200))`

#### `np.logical_and(x1, x2)`
- Combine conditions with AND logic  
Example: `np.logical_and(image[:,:,0] > 100, image[:,:,0] < 200)`

#### `np.logical_or(x1, x2)`
- Combine conditions with OR logic  
Example: `np.logical_or(image[:,:,0] < 50, image[:,:,2] > 200)`

#### `np.logical_not(x)`
- Negate boolean array  
Example: `np.logical_not(mask)`

#### `np.all(a, axis=2)`
- Check if all conditions are True across RGB channels  
Example: `np.all((image > 100) & (image < 200), axis=2)`

#### `np.any(a, axis=2)`
- Check if any condition is True across RGB channels  
Example: `np.any(image > 200, axis=2)`

## 2. Array Indexing & Modification

### Boolean Indexing
`image_array[mask] = new_value`  
Example: `image_array[(image_array[:,:,0] > 100) & (image_array[:,:,0] < 200)] = [255, 0, 0]`

### Channel Slicing
- Red: `image_array[:, :, 0]`  
- Green: `image_array[:, :, 1]`  
- Blue: `image_array[:, :, 2]`  
Example: `image_array[:, :, 0] += 50`

## 3. Clamping & Normalization

#### `np.clip(a, 0, 255)`
- Clamp values to valid RGB range  
Example: `np.clip(image_array, 0, 255)`

#### `array.astype(np.uint8)`
- Convert to proper image format  
Example: `image_array.astype(np.uint8)`

## 4. Arithmetic Operations

#### `np.add()`
Example: `np.add(image_array, 50)` (brightness)

#### `np.subtract()`
Example: `np.subtract(image_array, 30)` (darken)

#### `np.multiply()`
Example: `np.multiply(image_array, 1.2)` (contrast)

#### `np.divide()`
Example: `np.divide(image_array, 2)` (dim)

#### `np.dot()`
Example: `np.dot(image_array, [[1.2,0,0],[0,1.2,0],[0,0,1.2]])`

## 5. Copying & Structuring

#### `np.copy()`
Example: `copy_img = np.copy(image_array)`

#### `np.zeros_like()`
Example: `new_img = np.zeros_like(image_array)`

#### `np.ones_like()`
Example: `new_img = np.ones_like(image_array) * 255`