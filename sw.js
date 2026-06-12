const CACHE_NAME = 'jux-arcade-v1';
const ASSETS = [
  '/Learn/ARCADE.html',
  '/Learn/SNAKE.html',
  '/Learn/JuXYams.html',
  '/Learn/HOLDEM.TRAINING.html',
  '/Learn/DUNE.TAROT.PORN.html',
  '/Learn/DUNE.TAROT.GAME.html',
  '/Learn/DUNE.TAROT.html',
  '/Learn/MONOPOLY.html',
  '/Learn/SSS.html',
  '/Learn/CAVERN.html'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});
