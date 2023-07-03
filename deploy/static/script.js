// document.addEventListener('DOMContentLoaded', () => {
//     const canvas = document.getElementById('canvas');
//     const ctx = canvas.getContext('2d');
//     let isDrawing = false;
  
//     canvas.addEventListener('mousedown', startDrawing);
//     canvas.addEventListener('mousemove', draw);
//     canvas.addEventListener('mouseup', stopDrawing);
//     canvas.addEventListener('mouseout', stopDrawing);
  

//     // Add click event listener to the "Clear" button
//     const clearBtn = document.getElementById('clearBtn');
//     clearBtn.addEventListener('click', clearDrawing);

//     // Add click event listener to the "Save" button
//     const saveBtn = document.getElementById('saveBtn');
//     saveBtn.addEventListener('click', saveImage);

//     const uploadInput = document.getElementById('uploadInput');
//     uploadInput.addEventListener('change', handleUpload);
  
//     const predictBtn = document.getElementById('predictBtn');
//     predictBtn.addEventListener('click', predictImage);

//     function startDrawing(e) {
//       isDrawing = true;
//       draw(e);
//     }
  
//     function draw(e) {
//       if (!isDrawing) return;
  
//       const rect = canvas.getBoundingClientRect();
//       const x = e.clientX - rect.left;
//       const y = e.clientY - rect.top;
  
//       ctx.lineWidth = 30;
//       ctx.lineCap = 'round';
//       ctx.strokeStyle = '#000';
//       ctx.lineTo(x, y);
//       ctx.stroke();
//       ctx.beginPath();
//       ctx.moveTo(x, y);
//     }
  
//     function stopDrawing() {
//       isDrawing = false;
//       ctx.beginPath();
//     }

//     function clearDrawing() {
//       ctx.clearRect(0, 0, canvas.width, canvas.height);
//     }

//     // function saveImage() {
//     //   const image = canvas.toDataURL('image/png');
//     //   const link = document.createElement('a');
//     //   link.href = image;
//     //   link.download = 'drawing.png';
//     //   link.click();
//     // }
//     function saveImage() {
//       // Create a new canvas with white background
//       const newCanvas = document.createElement('canvas');
//       newCanvas.width = canvas.width;
//       newCanvas.height = canvas.height;
//       const newCtx = newCanvas.getContext('2d');
//       newCtx.fillStyle = '#fff';
//       newCtx.fillRect(0, 0, newCanvas.width, newCanvas.height);
    
//       // Draw the existing canvas on top of the new canvas
//       newCtx.drawImage(canvas, 0, 0);
    
//       // Convert the new canvas to a data URL and save the image
//       const image = newCanvas.toDataURL('image/png');
//       const link = document.createElement('a');
//       link.href = image;
//       link.download = 'drawing.png';
//       link.click();
//     }
    
//     function handleUpload(e) {
//       const file = e.target.files[0];
//       const reader = new FileReader();
  
//       reader.onload = function(event) {
//         const img = new Image();
//         img.onload = function() {
//           canvas.width = img.width;
//           canvas.height = img.height;
//           ctx.drawImage(img, 0, 0);
//         };
//         img.src = event.target.result;
//       };
  
//       reader.readAsDataURL(file);
//     }

//     async function predictImage() {
//       const image = canvas.toDataURL('image/png');
//       const response = await fetch('/predict', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body:JSON.stringify({ image: image })
//       });
  
//       if (response.ok) {
//         const result = await response.json();
//         const predictionResult = document.getElementById('predictionResult');
//         predictionResult.innerHTML = `Predicted Digit: ${result.prediction}`;
//       } else {
//         console.error('Error occurred during prediction.');
//       }
//     }
  

//   });
  



document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  let isDrawing = false;

  canvas.addEventListener('mousedown', startDrawing);
  canvas.addEventListener('mousemove', draw);
  canvas.addEventListener('mouseup', stopDrawing);
  canvas.addEventListener('mouseout', stopDrawing);

  // Add click event listener to the "Clear" button
  const clearBtn = document.getElementById('clearBtn');
  clearBtn.addEventListener('click', clearDrawing);

  // Add click event listener to the "Save" button
  const saveBtn = document.getElementById('saveBtn');
  saveBtn.addEventListener('click', saveImage);

  const uploadInput = document.getElementById('uploadInput');
  uploadInput.addEventListener('change', handleUpload);

  const predictBtn = document.getElementById('predictBtn');
  predictBtn.addEventListener('click', predictImage);

  function startDrawing(e) {
    isDrawing = true;
    draw(e);
  }

  function draw(e) {
    if (!isDrawing) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineWidth = 30;
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#000';
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x, y);
    ctx.stroke();
  }

  function stopDrawing() {
    isDrawing = false;
    ctx.beginPath();
  }

  function clearDrawing() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function saveImage() {
    // Create a new canvas with white background
    const newCanvas = document.createElement('canvas');
    newCanvas.width = canvas.width;
    newCanvas.height = canvas.height;
    const newCtx = newCanvas.getContext('2d');
    newCtx.fillStyle = '#fff';
    newCtx.fillRect(0, 0, newCanvas.width, newCanvas.height);

    // Draw the existing canvas on top of the new canvas
    newCtx.drawImage(canvas, 0, 0);

    // Convert the new canvas to a data URL and save the image
    const image = newCanvas.toDataURL('image/png');
    const link = document.createElement('a');
    link.href = image;
    link.download = 'drawing.png';
    link.click();
  }

  function handleUpload(e) {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = function(event) {
      const img = new Image();
      img.onload = function() {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
      };
      img.src = event.target.result;
    };

    reader.readAsDataURL(file);
  }

  async function predictImage() {
    const image = canvas.toDataURL('image/png');
    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: image })
    });

    if (response.ok) {
      const result = await response.json();
      const predictionResult = document.getElementById('predictionResult');
      predictionResult.innerHTML = `Predicted Digit: ${result.prediction}`;
    } else {
      console.error('Error occurred during prediction.');
    }
  }

});
