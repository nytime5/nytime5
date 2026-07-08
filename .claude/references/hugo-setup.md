# Hugo Setup & Infrastructure

## Framework
- **Hugo** hosted on **GitHub**, deployed via **Cloudflare Workers** (static assets). Pages is obsolete — do not reintroduce it.
- Cloudflare handles CDN, SSL, and DNS — do not add any configuration that conflicts with Cloudflare proxying
- Deploy config lives in committed [`wrangler.jsonc`](/wrangler.jsonc) (Worker `nytime5`, `assets.directory = public`). A committed config is required — without it, `wrangler deploy` re-runs auto-config and refuses to overwrite the existing Worker.
- Workers Builds **deploy command** must build then deploy: `npm run deploy` (i.e. `npx hugo && npx wrangler deploy`). `wrangler deploy` alone does not run Hugo, and Workers Builds ignores wrangler custom `build` commands.

## Directory Structure
```
/posts/          ← all article Markdown files (never move this)
/wiki/           ← fictional universe reference (people, orgs, places, events)
/assets/
  /css/          ← all stylesheets (never move this)
  /js/           ← all JavaScript (never move this)
/layouts/        ← Hugo templates
hugo.toml        ← Hugo configuration
CLAUDE.md        ← site-wide conventions
posts/CLAUDE.md  ← article-specific instructions
wiki/CLAUDE.md   ← wiki-specific instructions
```

## Hugo Configuration
`hugo.toml` uses module mounts to serve `/posts` as both content and static (for images). Posts are regular pages, not page bundles — multiple articles share a date directory.

## HTML Contract

CSS and JS are written against these class names. All templates must produce this structure regardless of any future framework migration.

```html
<article class="post">
  <header class="post-header">
    <h1 class="post-title">...</h1>
    <p class="post-meta">
      <time class="post-date">...</time>
    </p>
  </header>
  <div class="post-content">
    ...
  </div>
</article>
```

**Do not change these class names without also updating CSS and JS.**

## Framework Portability

The content layer (posts, images, front matter) is decoupled from the framework. Migrating to another SSG would require only:
- Replacing `hugo.toml` with the new framework's config
- Rewriting templates in `/layouts/`
- CSS, JS, images, and all post content remain untouched

Front matter uses standard YAML fields with no Hugo-specific fields inside post files.

## Cloudflare Notes

- Site is proxied through Cloudflare — do not hardcode IP addresses anywhere
- SSL is handled by Cloudflare — do not configure Hugo to force HTTPS redirects
- Caching is handled by Cloudflare — do not add aggressive cache headers in Hugo config that could conflict
