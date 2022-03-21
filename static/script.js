const imgBtn = document.querySelector('#img-btn');
const textBtn = document.querySelector('#text-btn');
const urlInput = document.querySelector('#url-input');
const baseUrl = window.location.origin;

imgBtn.onclick = () => {
  const imageUrl = urlInput.value;
  if (!imageUrl) {
    alert('Please enter a url');
    return;
  }
  const newUrl = `${baseUrl}/image?url=${imageUrl}`;
  window.open(newUrl, '_blank');
};

textBtn.onclick = () => {
  const imageUrl = urlInput.value;
  if (!imageUrl) {
    alert('Please enter text');
    return;
  }
  const newUrl = `${baseUrl}/text?url=${imageUrl}`;
  window.open(newUrl, '_blank');
};
