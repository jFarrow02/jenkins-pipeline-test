# Blob Stores

A **blob store** is storage for uploaded artifacts/components.
- Internal storage of binary files
- can be local or cloud storage
- can be used by multiple repositories or repository groups

## Location of Blob Store Config
`/opt/sonatype-work/blobs`: storage of all blob stores

## Blob Store Attribues
1. Type: Type of storage backend:
    - file: file-system based storage (see above)
    - S3: AWS S3 cloud-based storage (recommended for AWS-deployed nexus instances only)
2. State:
    - started: blob store is running
    - failed: blob store failed to initialize
3. Blob count: number of blobs currently stored
4. Size: Total size of all blobs
5. Available Space: space available in the blob store

## Things to note
- Blob stores can't be modified once created
- Blob store in use by a repo can't be deleted
- One repo is tied to a single blob store (cannot use multiple blob stores)
- Cannot re-assign a blob store to a repo once blob store is assigned
- How many blob stores to create?
- what sizes?
- how much space will each repo need?

## Assigning a Blob Store to a Repository in Nexus UI
1. Create a repository
2. Storage > Blob store > select blob store name