const CACHE = 'jux-arcade-v1';
const URLS = [
  'ARCADE.html',
  'SNAKE.html',
  'JuXYams.html',
  'MONOPOLY.html'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(URLS)));
  self.skipWaiting();
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
