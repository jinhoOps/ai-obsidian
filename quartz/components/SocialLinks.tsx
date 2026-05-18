import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

function SocialLinks({ displayClass }: QuartzComponentProps) {
  return (
    <div class={classNames(displayClass, "social-links")}>
      <hr />
      <ul>
        <li>
          <a href="https://github.com/jinhoOps/ai-obsidian" target="_blank" rel="noopener noreferrer">
             jinhoOps GitHub
          </a>
        </li>
      </ul>
    </div>
  )
}

SocialLinks.css = `
.social-links {
  margin-top: 2rem;
}

.social-links hr {
  border: none;
  border-top: 1px solid var(--lightgray);
  margin-bottom: 1rem;
}

.social-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.social-links li {
  margin-bottom: 0.5rem;
}

.social-links a {
  color: var(--darkgray);
  text-decoration: none;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.social-links a:hover {
  color: var(--secondary);
}
`

export default (() => SocialLinks) satisfies QuartzComponentConstructor
