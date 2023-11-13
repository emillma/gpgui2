export const ssr = false;

/** @type {import('./$types').PageLoad} */
export function load({ params, url }) {
    return {
        title: `Title for ${params.slug} goes here`,
        content: `Content for ${params.slug} goes here`
    };
}