const CACHE_VERSION = "2026.07.18.2";
const DISH_CACHE = `fiveish-dish-images-${CACHE_VERSION}`;
const DISH_IMAGE_PATH = "/assets/dishes/plain/";

self.addEventListener("install", (event) => {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(
      keys
        .filter((key) => key.startsWith("fiveish-dish-images-") && key !== DISH_CACHE)
        .map((key) => caches.delete(key))
    );
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (!url.pathname.includes(DISH_IMAGE_PATH) || !url.pathname.endsWith(".png")) return;

  event.respondWith((async () => {
    const cache = await caches.open(DISH_CACHE);
    const cached = await cache.match(request);
    if (cached) return cached;

    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  })());
});
