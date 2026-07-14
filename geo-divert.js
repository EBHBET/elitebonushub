/*
 * Geo-based CTA diversion for affiliate offers with country restrictions.
 *
 * Not yet included on any live page - nothing currently links 7BitCasino,
 * KatsuBet, or MiraxCasino individually. Wire this in via
 * <script src="/geo-divert.js" defer></script> once a review/CTA page for
 * one of those brands goes live.
 *
 * Usage: add these data attributes to any <a> CTA that should swap out for
 * visitors from a restricted country:
 *
 *   <a href="https://partner-link.example/abc123"
 *      data-geo-restrict="FR,ES,GB"
 *      data-geo-fallback-href="https://stake.com"
 *      data-geo-fallback-text="Claim at Stake &rarr;"
 *      class="cta-btn" rel="nofollow sponsored" target="_blank">
 *     Claim Bonus at Example Casino &rarr;
 *   </a>
 *
 * data-geo-restrict: comma-separated ISO 3166-1 alpha-2 codes this specific
 * offer does NOT accept, using exactly what the affiliate network discloses.
 * "FR" alone diverts mainland France without touching other French-speaking
 * countries - Morocco (MA), Senegal (SN), Ivory Coast (CI) etc. are
 * unaffected unless explicitly added to the list.
 *
 * data-geo-fallback-href / data-geo-fallback-text: the alternative CTA shown
 * instead - normally an already-reviewed casino with no restriction for that
 * visitor's country.
 *
 * Geo-IP source: ipapi.co (free tier, HTTPS, ~1,000 lookups/day). If traffic
 * outgrows that, swap the fetch URL for a paid provider or a server-side
 * lookup (e.g. Cloudflare's CF-IPCountry header, if the site ever fronts
 * through Cloudflare per the 2026-07-13 audit's recommendation).
 */
(function () {
  var restricted = document.querySelectorAll('[data-geo-restrict]');
  if (!restricted.length) return; // no restricted CTAs on this page, skip the lookup entirely

  fetch('https://ipapi.co/json/')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var country = data && data.country_code;
      if (!country) return;

      restricted.forEach(function (el) {
        var blocked = el.getAttribute('data-geo-restrict').split(',').map(function (c) { return c.trim(); });
        if (blocked.indexOf(country) === -1) return; // visitor's country isn't restricted for this offer

        var fallbackHref = el.getAttribute('data-geo-fallback-href');
        var fallbackText = el.getAttribute('data-geo-fallback-text');
        if (fallbackHref) el.setAttribute('href', fallbackHref);
        if (fallbackText) el.textContent = fallbackText;
        el.setAttribute('data-geo-diverted', country);
      });
    })
    .catch(function () {
      // Geo-IP lookup failed - fail open, leave original CTAs untouched rather than breaking the page
    });
})();
