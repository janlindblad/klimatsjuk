  const apiUrl = 'https://worldtimeapi.org/api/timezone/Europe/Stockholm';

  // Fetch the JSON, parse it, and put the week_number into the page
  fetch(apiUrl, { cache: 'no-store' })          // no caching – we want the freshest value
    .then(response => {
      if (!response.ok) throw new Error('Network response was not ok');
      return response.json();
    })
    .then(data => {
      // `data.week_number` holds the integer you need
      const weekEl = document.getElementById('week-number');
      weekEl.textContent = data.week_number;
    })
    .catch(err => {
      // Graceful fallback if the request fails
      console.error('Error fetching week number:', err);
      document.getElementById('week-number').textContent = '—';
    });
